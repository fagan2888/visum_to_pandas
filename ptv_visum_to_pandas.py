import codecs
import pandas as pd

# semantics
COL_DELIMITER = ";"
TABLE_NAME_HEADER = "* Table: "
COL_DEF_HEADER = "$"

#paths
NETPATH = "./test/MOMM_net.net"
OUTPATH = "./test/data/"

def parse_net():

    _table_flag = False

    with codecs.open(NETPATH, encoding='utf-8', errors='ignore') as net:

        for line in net:
            if line.startswith(TABLE_NAME_HEADER):
                # new table
                table_name = line.split(":")[-1][1:-1]

            if line[0] == COL_DEF_HEADER:
                # line with column names
                _table_flag = True
                data = list()  # initialize data
                try:
                    cols = line.split(":")[1].split(COL_DELIMITER)
                except:
                    cols = line.split(COL_DELIMITER)
            if line == '\n':
                _table_flag = False
                if len(data) > 0:
                    # only if table is not empty
                    pd.DataFrame(data, columns=cols).to_csv(OUTPATH+table_name+".csv")
            if _table_flag and line[0] != COL_DEF_HEADER:
                data.append(line.split(COL_DELIMITER))


if __name__ == "__main__":
    parse_net()







