import os
from testFile.getPath import get_Path
from xlrd import open_workbook



'''
读取用例
'''

path = get_Path()
class readExcel():

    def get_row(self,xls_name,sheet_name): # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        '''获取除一行所有行数据'''
        cls = []
        xlsPath = path + '\case_excel\\' + xls_name
        file = open_workbook(xlsPath) # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name) # 获得打开Excel的sheet
        nrows = sheet.nrows # 获取这个sheet有效行数
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != 'CaseID': # 如果这个Excel的这个sheet的第i行的第一列不等于'CaseID'那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls

    def get_col(self,xls_name,sheet_name):
        '''获取ExpectResult这一列数据'''
        cls = []
        xlsPath = path + '\case_excel\\' + xls_name
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheet_name)
        ncols = sheet.ncols # 获取这个sheet有效列数
        for i in range(ncols):
            if sheet.row_values(0)[i] == 'ExpectResult': # 如果这个Excel得这sheet的第1行的第i列等于'ExpectResult'那么我们就把这行数据添加到cls[]
                cls.append(sheet.col_values(i))
        return cls[0][1:] # 返回cls中第一个数组中嵌套的数组第2个元素，以便于去除'ExpectResult'





if __name__ == '__main__':  # 测试
    print(readExcel().get_row('login_case.xlsx', 'login'))
    print(readExcel().get_col('login_case.xlsx', 'login'))
