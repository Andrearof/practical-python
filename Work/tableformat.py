# Exercise 4.5: An Extensibility Problem


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emite a single row of data
        """
        raise NotImplementedError()
