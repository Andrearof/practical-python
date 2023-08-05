# Exercise 4.7: Polymorphism in Action


def create_formatter(format: str) -> "TableFormatter":
    formatter: TableFormatter
    match format:
        case "txt":
            formatter = TextTableFormatter()
        case "csv":
            formatter = CSVTableFormatter()
        case "html":
            formatter = HTMLTableFormatter()
        case other:
            raise RuntimeError(f"Unknown format {format}")
    return formatter


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


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plai-text format
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format
    """

    def headings(self, headers):
        print("<tr>", end="")
        for h in headers:
            print(f"<th>{h}</th>", end="")
        print("</tr>", end="")
        print()

    def row(self, rowdata):
        print("<tr>", end="")
        for r in rowdata:
            print(f"<th>{r}</th>", end="")
        print("</tr>", end="")
        print()
