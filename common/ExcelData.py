# coding:utf-8
import xlrd


class Excel:
    def __init__(self):
        self.test_data_path = '../testdata/testdata.xlsx'

    def open_excel(self,file):
        '''读取excel文件'''
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            raise e

    def excel_table(self,file, sheetName):
        '''装载list'''
        data = self.open_excel(file)
        # 通过工作表名称，获取到一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取行数
        Trows = table.nrows
        # 获取 第一行数据
        Tcolnames = table.row_values(0)
        lister = []
        for rownumber in range(1,Trows):
            row = table.row_values(rownumber)
            if row:
                app = {}
                for i in range(len(Tcolnames)):
                    app[Tcolnames[i]] = row[i]
                lister.append(app)
        return lister

    def get_list(self,sheetname):
        try:
            data_list = self.excel_table(self.test_data_path, sheetname)
            assert len(data_list)>=0,'excel标签页:'+sheetname+'为空'
            return data_list
        except Exception as e:
            raise e