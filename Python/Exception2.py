def purchase_item(price,card_no):

    if price<0:

        raise Exception("invalid price")
    if card_no not in [101,102,103]:
        raise Exception("wrong choice")

try:
    purchase_item(1200,100)

except Exception as e:

    if str(e)=="invalid price":
        print("1")
    if str(e)=="wrong choice":
        print("2")
