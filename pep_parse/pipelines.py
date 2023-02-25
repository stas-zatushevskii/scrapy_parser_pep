from .settings import BASE_DIR, FILE_NAME, RESULTS


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_statuses = {}

    def process_item(self, item, spider):
        if item['status'] in self.pep_statuses:
            self.pep_statuses[item['status']] += 1
        else:
            self.pep_statuses[item['status']] = 0
        return item

    def close_spider(self, spider):
        with open(BASE_DIR / RESULTS / FILE_NAME, mode='w', encoding='utf-8'
                  ) as file:
            file.write('Статус,Количество\n')
            for status in self.pep_statuses.keys():
                file.write(f'{status},{self.pep_statuses[status]}\n')
            total = sum(self.pep_statuses.values())
            file.write(f'Total,{total}\n')
