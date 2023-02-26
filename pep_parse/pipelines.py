from .settings import BASE_DIR, FILE_NAME, RESULTS


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_statuses = {}

    def process_item(self, item, spider):
        self.pep_statuses[item['status']] = self.pep_statuses.get(
            item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        with open(BASE_DIR / RESULTS / FILE_NAME, mode='w', encoding='utf-8'
                  ) as file:
            file.write('Статус,Количество\n')
            for status in self.pep_statuses.keys():
                file.write(f'{status},{self.pep_statuses[status]}\n')
            total = sum(self.pep_statuses.values())
            file.write(f'Total,{total}\n')
