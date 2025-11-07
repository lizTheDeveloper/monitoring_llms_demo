"""
Production Monitoring Dashboard for DeepChecks.

This module provides enhanced reporting, visualization, and alert configuration
for production monitoring of data quality and model performance.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd
from deepchecks.core import CheckResult, SuiteResult

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AlertConfig:
    """Configuration for alert thresholds."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize alert configuration."""
        self.config_path = config_path or 'alert_config.json'
        self.default_thresholds = {
            'data_integrity': {
                'missing_values_threshold': 0.05,  # 5% missing values
                'duplicates_threshold': 0.01,  # 1% duplicates
                'data_quality_score': 0.8,  # Minimum quality score
            },
            'data_drift': {
                'drift_score_threshold': 0.2,  # Maximum drift score
                'feature_drift_threshold': 0.15,  # Per-feature drift
                'label_drift_threshold': 0.1,  # Label distribution drift
            },
            'model_performance': {
                'accuracy_threshold': 0.7,  # Minimum accuracy
                'performance_degradation': 0.1,  # Max degradation from baseline
            }
        }
        self.load_config()
    
    def load_config(self):
        """Load alert configuration from file or use defaults."""
        if Path(self.config_path).exists():
            try:
                with open(self.config_path, 'r') as f:
                    self.thresholds = json.load(f)
                logger.info(f"Loaded alert configuration from {self.config_path}")
            except Exception as e:
                logger.warning(f"Failed to load config: {e}. Using defaults.")
                self.thresholds = self.default_thresholds
        else:
            self.thresholds = self.default_thresholds
            self.save_config()
    
    def save_config(self):
        """Save current configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.thresholds, f, indent=2)
            logger.info(f"Saved alert configuration to {self.config_path}")
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
    
    def get_threshold(self, category: str, metric: str) -> float:
        """Get threshold for a specific metric."""
        return self.thresholds.get(category, {}).get(metric, 0.0)


class MonitoringDashboard:
    """Enhanced monitoring dashboard with reporting and alerting."""
    
    def __init__(self, alert_config: Optional[AlertConfig] = None):
        """Initialize monitoring dashboard."""
        self.alert_config = alert_config or AlertConfig()
        self.results_history: List[Dict] = []
        self.alerts: List[Dict] = []
        self.output_dir = Path('monitoring_results')
        self.output_dir.mkdir(exist_ok=True)
    
    def analyze_result(self, result: SuiteResult, suite_name: str, 
                      timestamp: Optional[datetime] = None) -> Dict:
        """
        Analyze a DeepChecks suite result and extract metrics.
        
        Args:
            result: DeepChecks SuiteResult
            suite_name: Name of the suite
            timestamp: Timestamp of the run
            
        Returns:
            Dictionary with analysis results
        """
        if timestamp is None:
            timestamp = datetime.now()
        
        analysis = {
            'timestamp': timestamp.isoformat(),
            'suite_name': suite_name,
            'total_checks': len(result.results),
            'passed_checks': sum(1 for r in result.results if r.passed_conditions()),
            'failed_checks': sum(1 for r in result.results if not r.passed_conditions()),
            'warnings': sum(1 for r in result.results if r.have_warnings()),
            'checks': []
        }
        
        # Analyze individual checks
        for check_result in result.results:
            check_analysis = {
                'name': check_result.get_header(),
                'passed': check_result.passed_conditions(),
                'has_warnings': check_result.have_warnings(),
                'conditions': []
            }
            
            # Extract condition results
            if hasattr(check_result, 'conditions_results'):
                for condition in check_result.conditions_results:
                    check_analysis['conditions'].append({
                        'name': condition.get('name', 'Unknown'),
                        'passed': condition.get('passed', False),
                        'value': condition.get('value', None)
                    })
            
            analysis['checks'].append(check_analysis)
        
        # Store in history
        self.results_history.append(analysis)
        
        # Check for alerts
        self._check_alerts(analysis)
        
        return analysis
    
    def _check_alerts(self, analysis: Dict):
        """Check if any metrics exceed alert thresholds."""
        suite_name = analysis['suite_name']
        
        # Check data integrity alerts
        if 'data_integrity' in suite_name.lower():
            for check in analysis['checks']:
                if not check['passed']:
                    self._create_alert(
                        level='warning',
                        category='data_integrity',
                        message=f"Data integrity check failed: {check['name']}",
                        details=check
                    )
        
        # Check data drift alerts
        if 'drift' in suite_name.lower() or 'validation' in suite_name.lower():
            failed_checks = [c for c in analysis['checks'] if not c['passed']]
            if failed_checks:
                self._create_alert(
                    level='critical',
                    category='data_drift',
                    message=f"Data drift detected: {len(failed_checks)} checks failed",
                    details={'failed_checks': failed_checks}
                )
        
        # Check model performance alerts
        if 'model' in suite_name.lower() or 'evaluation' in suite_name.lower():
            if analysis['failed_checks'] > 0:
                self._create_alert(
                    level='warning',
                    category='model_performance',
                    message=f"Model performance issues: {analysis['failed_checks']} checks failed",
                    details=analysis
                )
    
    def _create_alert(self, level: str, category: str, message: str, details: Dict):
        """Create an alert."""
        alert = {
            'timestamp': datetime.now().isoformat(),
            'level': level,
            'category': category,
            'message': message,
            'details': details
        }
        self.alerts.append(alert)
        logger.warning(f"ALERT [{level.upper()}] {category}: {message}")
    
    def generate_summary_report(self) -> str:
        """Generate a summary report of all monitoring results."""
        if not self.results_history:
            return "No monitoring results available."
        
        report_lines = [
            "=" * 80,
            "DEEPCHECKS MONITORING SUMMARY REPORT",
            "=" * 80,
            f"Generated: {datetime.now().isoformat()}",
            f"Total Runs: {len(self.results_history)}",
            "",
        ]
        
        # Overall statistics
        total_checks = sum(r['total_checks'] for r in self.results_history)
        total_passed = sum(r['passed_checks'] for r in self.results_history)
        total_failed = sum(r['failed_checks'] for r in self.results_history)
        
        report_lines.extend([
            "OVERALL STATISTICS",
            "-" * 80,
            f"Total Checks Run: {total_checks}",
            f"Passed: {total_passed} ({total_passed/total_checks*100:.1f}%)",
            f"Failed: {total_failed} ({total_failed/total_checks*100:.1f}%)",
            "",
        ])
        
        # Recent runs
        report_lines.extend([
            "RECENT RUNS",
            "-" * 80,
        ])
        
        for result in self.results_history[-5:]:  # Last 5 runs
            report_lines.append(
                f"{result['timestamp']} - {result['suite_name']}: "
                f"{result['passed_checks']}/{result['total_checks']} passed"
            )
        
        report_lines.append("")
        
        # Active alerts
        if self.alerts:
            report_lines.extend([
                "ACTIVE ALERTS",
                "-" * 80,
            ])
            
            critical_alerts = [a for a in self.alerts if a['level'] == 'critical']
            warning_alerts = [a for a in self.alerts if a['level'] == 'warning']
            
            report_lines.append(f"Critical: {len(critical_alerts)}")
            report_lines.append(f"Warnings: {len(warning_alerts)}")
            report_lines.append("")
            
            for alert in self.alerts[-10:]:  # Last 10 alerts
                report_lines.append(
                    f"[{alert['level'].upper()}] {alert['timestamp']} - "
                    f"{alert['category']}: {alert['message']}"
                )
        else:
            report_lines.append("No active alerts.")
        
        report_lines.append("")
        report_lines.append("=" * 80)
        
        return "\n".join(report_lines)
    
    def save_reports(self):
        """Save all reports to files."""
        # Save summary report
        summary_path = self.output_dir / 'monitoring_summary.txt'
        with open(summary_path, 'w') as f:
            f.write(self.generate_summary_report())
        logger.info(f"Saved summary report to {summary_path}")
        
        # Save results history as JSON
        history_path = self.output_dir / 'results_history.json'
        with open(history_path, 'w') as f:
            json.dump(self.results_history, f, indent=2)
        logger.info(f"Saved results history to {history_path}")
        
        # Save alerts as JSON
        if self.alerts:
            alerts_path = self.output_dir / 'alerts.json'
            with open(alerts_path, 'w') as f:
                json.dump(self.alerts, f, indent=2)
            logger.info(f"Saved alerts to {alerts_path}")
        
        # Generate CSV report
        self._generate_csv_report()
    
    def _generate_csv_report(self):
        """Generate CSV report of results history."""
        if not self.results_history:
            return
        
        rows = []
        for result in self.results_history:
            rows.append({
                'timestamp': result['timestamp'],
                'suite_name': result['suite_name'],
                'total_checks': result['total_checks'],
                'passed_checks': result['passed_checks'],
                'failed_checks': result['failed_checks'],
                'warnings': result['warnings'],
                'pass_rate': result['passed_checks'] / result['total_checks'] if result['total_checks'] > 0 else 0
            })
        
        df = pd.DataFrame(rows)
        csv_path = self.output_dir / 'monitoring_history.csv'
        df.to_csv(csv_path, index=False)
        logger.info(f"Saved CSV report to {csv_path}")
    
    def print_dashboard(self):
        """Print monitoring dashboard to console."""
        print("\n" + self.generate_summary_report() + "\n")


def create_alert_config_file(config_path: str = 'alert_config.json'):
    """Create a default alert configuration file."""
    config = AlertConfig(config_path)
    logger.info(f"Created default alert configuration at {config_path}")
    return config


if __name__ == '__main__':
    """Example usage of the monitoring dashboard."""
    # Create alert configuration
    alert_config = create_alert_config_file()
    
    # Initialize dashboard
    dashboard = MonitoringDashboard(alert_config)
    
    # Example: Simulate some results (in real usage, pass actual SuiteResult objects)
    print("Monitoring Dashboard Example")
    print("=" * 80)
    print("\nTo use the dashboard with actual DeepChecks results:")
    print("  from monitoring_dashboard import MonitoringDashboard")
    print("  dashboard = MonitoringDashboard()")
    print("  analysis = dashboard.analyze_result(suite_result, 'data_integrity')")
    print("  dashboard.save_reports()")
    print("  dashboard.print_dashboard()")
    print("\nAlert configuration saved to alert_config.json")
    print("You can modify thresholds in that file.")

