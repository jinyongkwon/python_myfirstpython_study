import pandas as pd
import pymysql as pm


def mysql():
    db = pm.connect(host='localhost', port=3306, user='root', password='12qwer#$', db='dat_ai', charset='utf8')
    sql = """
        select code,brand, name, price
        from pp_part_price ppp
                 join (select name,brand,code,part_seq
                       from pp_part pp
                                join pp_part_code ppc on pp.seq = ppc.part_seq
                       where pp.brand = 'Benz'
                          or pp.brand = 'landrover') a
        on ppp.part_seq = a.part_seq 
    """
    with db:
        with db.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
            return result


def print_hi():
    # sql_result = mysql()
    df = pd.read_csv("20220901.csv")
    df.소비자가격 = df.소비자가격.astype(float)
    exp = "소비자가격%1 > 0"
    exp2 = "소비자가격 == 0"
    test1 = df.query(exp)
    test2 = df.query(exp2)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    # index = test2.columns.difference(['Unnamed: 0'])
    index = test1.columns.difference(['Unnamed: 0'])
    # test2 = test2[index]
    test1 = test1[index]
    print(test1)

    # csv_result = list(zip(test2['품목'].tolist(), test2['품목명'].tolist()))
    # result = []
    # for csv in csv_result:
    #     for sql in sql_result:
    #         if csv[0] == sql[0] and csv[1] == sql[1]:
    #             result.append(csv)
    # sql_result = pd.DataFrame(sql_result, columns=["품목", "품목명"])
    # result = pd.DataFrame(result, columns=["품목", "품목명"])

    excel = pd.ExcelWriter(f"test.xlsx")
    test1.to_excel(excel, "크롤링 소수점 row")
    # test2.to_excel(excel, "csv인덱스")
    # test2 = test2.reset_index(drop=True)
    # test2.to_excel(excel, "인덱스 재정의")
    # sql_result.to_excel(excel, "sql 쿼리 결과")
    # result.to_excel(excel, "결과")
    excel.save()
    excel.close()


if __name__ == '__main__':
    print_hi()
