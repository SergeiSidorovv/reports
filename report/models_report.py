from collections import defaultdict


class PerformanceReport:
    def generate_report(self, rows: list) -> list:
        performance_by_position = defaultdict(list)
        for row in rows:
            position = row['position']
            performance = float(row['performance'])
            performance_by_position[position].append(performance) 

        report_data = self.set_average_performance(performance_by_position)
        return report_data


    @staticmethod
    def set_average_performance(performance_by_position: defaultdict) -> list:     
        average_performance_list = []
        for keys, values in performance_by_position.items():
            average_performance = round(sum(values) / len(values), 2)
            average_performance_list.append((keys, average_performance))
            average_performance_list.sort(key=lambda x: x[1], reverse=True)
        return average_performance_list
