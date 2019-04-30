
from django.db import connections

class DbUtil(object) :

    connection = None;
    cursor = None;


    def exeQuery(self, query, data=None):


        query = str(query).strip();
        queryTypePoint = query.find(" ");
        queryType = query[0:queryTypePoint];

        reVal = None;

        if queryType.lower() == "select" :
            reVal = self.exeGet(query, data);
            pass;
        elif queryType.lower() == "insert" :
            self.exeSet(query, data);
            pass;
        elif queryType.lower() == "update" :
            self.exeSet(query, data);
            pass;
        elif queryType.lower() == "delete" :
            self.exeSet(query, data);
            pass;

        else :
            pass;



        return reVal;



    def exeGet(self, query, data):
        self.connection = connections['default'];
        self.cursor = self.connection.cursor();

        c = self.cursor;
        c.execute(query, data);

        fieldnames = [name[0] for name in c.description];

        data = c.fetchall();

        reVal = [];

        if len(data) > 0:
            for row in data :
                reValColume = {};
                cntColume = 0;
                for rowColume in row:
                    reValColume[fieldnames[cntColume]] = rowColume;
                    cntColume+=1;

                    pass;
                pass;

                reVal.append(reValColume);
            pass;


        print(reValColume);

        self.connection.close();
        return reVal;

    def exeSet(self, query, data):
        self.connection = connections['default'];
        self.cursor = self.connection.cursor();
        c = self.cursor;
        c.execute(query, data);


        self.connection.close();