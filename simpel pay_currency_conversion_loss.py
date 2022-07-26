def euro_to_ils(euro):
    euro_to_ils_rate = float(input("Please enter the EUR to ILS exchange rate: "))
    ils = euro * euro_to_ils_rate
    print(f'{euro} EUR is {ils} ILS')
    return ils

def ils_to_czk(ils):
    ils_to_czk_rate = float(input("Please enter the ILS to CZK exchange rate: "))
    czk = ils * ils_to_czk_rate
    print(f'{ils} ILS is {czk} CZK')
    return czk

def euro_to_czk(euro):
    euro_to_czk_rate = float(input("Please enter the EUR to CZK exchange rate (from česká spořitelna): "))
    czk = euro * euro_to_czk_rate
    print(f'{euro} EUR is {czk} CZK')
    return czk

def calculate_loss(czk_from_ils, czk_from_euro):
    loss = czk_from_ils - czk_from_euro
    print(f'The loss is {loss} CZK')

def main():
    euro = int(input("Please enter the amount of EUR you would like to transfer: "))
    ils = euro_to_ils(euro)
    czk_from_ils = ils_to_czk(ils)
    czk_from_euro = euro_to_czk(euro)
    calculate_loss(czk_from_ils, czk_from_euro)

main()
