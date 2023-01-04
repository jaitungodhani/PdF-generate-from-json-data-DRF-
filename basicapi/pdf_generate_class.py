
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO


class BalanceSheet:
    def __init__(self, cash_in_bank, total_current_assets, total_assets, net_income, opening_balance_equity, \
                    owner_loan, retained_earnings, total_shareholders_equity, total_liabilities_and_equity, today_date, \
                        documentTitle, title):
        self.cash_in_bank = cash_in_bank
        self.total_current_assets = total_current_assets
        self.total_assets = total_assets
        self.net_income = net_income
        self.opening_balance_equity = opening_balance_equity
        self.owner_loan = owner_loan
        self.total_shareholders_equity = total_shareholders_equity
        self.total_liabilities_and_equity = total_liabilities_and_equity
        self.today_date = today_date
        self.retained_earnings = retained_earnings
        self.documentTitle = documentTitle
        self.title = title

    def generate_pdf(self):
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle(self.documentTitle)
        pdf.setFont("Helvetica", 18)
        pdf.drawCentredString(300, 808, self.title)
        pdf.setFont("Helvetica", 12)
        pdf.drawCentredString(300, 785, self.documentTitle)
        pdf.drawCentredString(300, 770, self.today_date)
        pdf.line(30, 750, 550, 750)
        pdf.drawCentredString(530, 735, "TOTAL")
        pdf.line(30, 730, 550, 730)
        pdf.drawCentredString(50, 715, "Assets")
        pdf.drawCentredString(75, 700, "Current Assets")
        pdf.drawCentredString(76, 685, "Cash in bank")
        pdf.drawCentredString(530, 685, str(self.cash_in_bank))
        pdf.setStrokeColorRGB(0.54,0.55,0.54)
        pdf.line(30, 680, 550, 680)
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawCentredString(90, 665, "Total Current Assets")
        pdf.drawCentredString(530, 665, str(self.total_current_assets))
        pdf.line(30, 660, 550, 660)
        pdf.drawCentredString(65, 645, "Total Assets")
        pdf.drawCentredString(530, 645, str(self.total_assets))
        pdf.setStrokeColorRGB(0,0,0)
        pdf.line(30, 640, 550, 640)
        pdf.line(30, 637, 550, 637)
        pdf.setFont("Helvetica", 12)
        pdf.drawCentredString(125, 623, "Liabilities and shareholder's equity")
        pdf.drawCentredString(95, 608, "Shareholders' equity:")
        pdf.drawCentredString(76, 595, "Net Income")
        pdf.drawCentredString(530, 595, str(self.net_income))
        pdf.drawCentredString(110, 580, "Opening Balance Equity")
        pdf.drawCentredString(530, 580, str(self.opening_balance_equity))
        pdf.drawCentredString(83, 565, "Owner's Loan")
        pdf.drawCentredString(530, 565, str(self.owner_loan))
        pdf.drawCentredString(95, 550, "Retained Earnings")
        pdf.drawCentredString(530, 550, str(self.retained_earnings))
        pdf.setFont("Helvetica-Bold", 12)
        pdf.setStrokeColorRGB(0.54,0.55,0.54)
        pdf.line(30, 545, 550, 545)
        pdf.drawCentredString(112, 530, "Total shareholders' equity")
        pdf.drawCentredString(530, 530, str(self.total_shareholders_equity))
        pdf.line(30, 525, 550, 525)
        pdf.drawCentredString(104, 510, "Total liabilities and equity")
        pdf.drawCentredString(530, 510, str(self.total_liabilities_and_equity))
        pdf.setStrokeColorRGB(0,0,0)
        pdf.line(30, 505, 550, 505)
        pdf.showPage()
        pdf.save()

        buffer.seek(0)
        
        return buffer


class ProfitandLoss:
    def __init__(self, revenue_general, commissions_and_fees, office_expenses, other_selling_expenses , \
                    from_date, to_date, title, documentTitle):
        self.revenue_general = revenue_general
        self.commissions_and_fees = commissions_and_fees
        self.office_expenses = office_expenses
        self.other_selling_expenses = other_selling_expenses
        self.from_date = from_date
        self.to_date = to_date
        self.total_income = revenue_general
        self.total_expenses = round(commissions_and_fees + office_expenses + other_selling_expenses, 2)
        self.net_earnings = round(self.revenue_general - self.total_expenses, 2)
        self.documentTitle = documentTitle
        self.title = title

    def generate_pdf(self):
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle(self.documentTitle)
        pdf.setFont("Helvetica", 18)
        pdf.drawCentredString(300, 808, self.title)
        pdf.setFont("Helvetica", 12)
        pdf.drawCentredString(300, 785, self.documentTitle)
        pdf.drawCentredString(300, 770, self.from_date + " - " + self.to_date)
        pdf.line(30, 750, 550, 750)
        pdf.drawCentredString(530, 735, "TOTAL")
        pdf.line(30, 730, 550, 730)
        pdf.drawCentredString(50, 715, "Income")
        pdf.drawCentredString(90, 700, "Revenue - General")
        pdf.drawCentredString(530, 700, str(self.revenue_general))
        pdf.setStrokeColorRGB(0.54,0.55,0.54)
        pdf.line(30, 695, 550, 695)
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawCentredString(66, 680, "Total income")
        pdf.drawCentredString(530, 680, str(self.total_income))
        pdf.line(30, 675, 550, 675)
        pdf.setFont("Helvetica", 12)
        pdf.drawCentredString(73, 660, "GROSS PROFIT")
        pdf.drawCentredString(530, 660, str(self.total_income))
        pdf.drawCentredString(55, 645, "Expenses")
        pdf.drawCentredString(100, 630, "Commissions and fees")
        pdf.drawCentredString(530, 630, str(self.commissions_and_fees))
        pdf.drawCentredString(82, 615, "Other expenses")
        pdf.drawCentredString(530, 615, str(self.office_expenses))
        pdf.drawCentredString(100, 600, "Other selling expenses")
        pdf.drawCentredString(530, 600, str(self.other_selling_expenses))
        pdf.line(30, 595, 550, 595)
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawCentredString(75, 580, "Total Expenses")
        pdf.drawCentredString(530, 580, str(self.total_expenses))
        pdf.line(30, 575, 550, 575)
        pdf.drawCentredString(75, 560, "NET EARNINGS")
        pdf.drawCentredString(530, 560, str(self.net_earnings))
        pdf.setStrokeColorRGB(0,0,0)
        pdf.line(30, 555, 550, 555)
        pdf.line(30, 552, 550, 552)
        pdf.showPage()
        pdf.save()

        buffer.seek(0)
        
        return buffer
