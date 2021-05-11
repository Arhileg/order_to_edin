import xlrd


EMPTY_CELL = xlrd.empty_cell.ctype
CELL_TEXT = xlrd.XL_CELL_TEXT
CELL_NUMBER = xlrd.XL_CELL_NUMBER


def read(file):
    """Read table to order to site EDIN"""
    book = xlrd.open_workbook(file)
    # print("The number of worksheets is {0}".format(book.nsheets))
    # print("Worksheet name(s): {0}".format(book.sheet_names()))
    sh = book.sheet_by_index(0)
    # print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    result_list = []
    for rx in range(sh.nrows):
        row = sh.row(rx)
        if row[4].ctype == CELL_TEXT and row[5].ctype == CELL_NUMBER and row[5].value != 0.0:
            item = dict()
            item['row'] = row[1].value
            item['group'] = row[2].value
            item['name'] = row[3].value
            item['barcode'] = row[4].value
            item['qtypack'] = row[5].value
            item['qty'] = row[6].value
            item['ppp'] = row[7].value
            result_list.append(item)
    return result_list


if __name__=="__main__":
    file = r'ВІММ-БІЛЛЬ-ДАНН заказник март21.xls'
    print(read(file))
