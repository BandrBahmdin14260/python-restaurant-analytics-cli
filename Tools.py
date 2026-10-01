import pandas as pd
import datetime
import time

'''
Staff Performance - 


Executive Summary Method: Summary_Data() +
Best_Days: Peak Hours: +
Search_Bills: By date,time,staff,money +
Display: +
'''


def Read_Data():
    data = pd.read_csv("data/restaurant_data_large.csv")
    return data


def get_Staff():
    data = Read_Data()
    data = list(data['staff_name'].value_counts().items())
    return data


def get_Anything(order: str):
    data = Read_Data()
    return data[order]


def columns_Data():
    data = Read_Data()

    # 1. الترويسة وعدد الأسطر والأعمدة
    output = (
        f"\n----------------------------------------\n"
        f"        📊 DATASET STRUCTURE OVERVIEW   \n"
        f"----------------------------------------\n"
        f"+ Total Records (Rows) : {len(data)}\n"
        f"+ Total Features (Cols): {len(data.columns)}\n"
        f"----------------------------------------\n"
        f"{'Column Name':<20} | {'Type':<10} \n"
        f"----------------------------------------\n"
    )

    for i in range(len(data.columns)):
        col_name = data.columns[i]
        col_type = str(data[col_name].dtype)
        output += f"{col_name:<20} | {col_type:<10}\n"
    output += "----------------------------------------\n"
    return output
def get_time():
    data = Read_Data()
    return data["time"]


def get_Hours():
    data = Read_Data()
    return data["order_time"]


def get_Payment():
    data = Read_Data()
    data = data["payment_method"]
    return data


def get_TotalRevenue():
    data = Read_Data()
    amount = data["total_amount_sar"].sum()
    return amount


def get_mostUsed_paymentTitle():
    data = get_Payment()
    top_item = data.value_counts().idxmax()
    return top_item


def get_orderId():
    data = Read_Data()
    return data["order_id"]


def get_TotalOrders():
    data = Read_Data()
    orders = data["order_id"].count()
    return orders


def get_avg_OrderValues():
    avg = get_TotalRevenue() / get_TotalOrders()
    return avg


def get_rating():
    data = Read_Data()
    rating = data["customer_rating"]
    return rating


def get_location():
    data = Read_Data()
    location = data["branch"]
    return location


def avr_rating():
    rating = get_rating()
    rating = rating.mean()
    return rating


def percent_payment():
    top_count = get_Payment().value_counts().max()
    percent_amount = top_count / get_TotalOrders()
    return int(percent_amount * 100)


def Analysis_Branch():
    data = get_location()
    maxBranch = data.value_counts().max()
    maxBranch_Br = data.value_counts().idxmax()

    minBranch = data.value_counts().min()
    minBranch_Br = data.value_counts().idxmin()
    mean = round(data.value_counts().mean(), 2)
    dictMessage = {"max": [maxBranch, maxBranch_Br]
        , "min": [minBranch, minBranch_Br]
        , "mean": mean}
    return dictMessage


def searchOrder(Order):
    data = get_orderId()
    orderArray = list(data.items())
    for i in range(len(orderArray)):
        if orderArray[i][1] == Order:
            return True
    return False


def Order_Info(Order: str):
    Order_Card = ""
    if not Order:
        Order = input("Enter Order ID: ")
    if searchOrder(Order):
        data = Read_Data()
        matching_rows = data[data["order_id"] == Order].iloc[0]
        Order_Card += (f"-----------------------------\n"
                       f"ORDER CARD: {matching_rows['order_id']}\n"
                       f"Branch : {matching_rows['branch']}\n"
                       f"Date : {matching_rows['order_date']}\n"
                       f"Time : {matching_rows['order_time']}\n"
                       f"Day : {matching_rows['day_of_week']}\n"
                       f"Order Type : {matching_rows['order_type']}\n"
                       f"-----------------------------\n"
                       f"Item : {matching_rows['item_name']} (x{matching_rows['quantity']})\n"
                       f"Payment     : {matching_rows['payment_method']}\n"
                       f"Net Amount  : {matching_rows['net_amount_sar']} SAR\n"
                       f"-----------------------------\n"
                       f"Staff Name : {matching_rows['staff_name']}\n"
                       f"-----------------------------\n")

        return Order_Card
    else:
        return "Not Found"
    pass


def bestOrder():
    data = get_Anything("item_name")
    best3Orders = (data.value_counts().head(3)).items()
    best3Orders = list(best3Orders)
    return best3Orders


def Analysis_Time(num=3):
    data = get_Anything("order_time")
    TimeList = list(data.value_counts().head(num).items())
    return TimeList


def Analysis_Days(num=3):
    data = get_Anything("day_of_week")
    DayList = list(data.value_counts().head(num).items())
    return DayList


def PeakTime_Branch():
    Branch = Analysis_Branch()
    TimeList = Analysis_Time()
    BestOrders = bestOrder()

    PeakMessage = f"\n-----------------------------\n"
    PeakMessage += f"BRANCH & PEAK TIME REPORT"
    PeakMessage += (f"\n-----------------------------\n"
                    f"- BRANCH PERFORMANCE:\n"
                    f"\t* Top Branch = {Branch["max"][1]} by {Branch["max"][0]} times \n"
                    f"\t* Lowest Branch = {Branch["min"][1]} by {Branch["min"][0]} times\n"
                    f"\t* Average = {Branch["mean"]}\n\n"
                    f"- TOP PEAK HOURS:\n")
    for i in range(len(TimeList)):
        PeakMessage += f"\t* {TimeList[i][0]} -> {TimeList[i][1]} times\n"

    PeakMessage += f"\n- TOP POPULAR ITEMS:\n"
    for i in range(len(BestOrders)):
        PeakMessage += f"\t* {BestOrders[i][0]} -> {BestOrders[i][1]} times\n"

    return PeakMessage


def Summary_Data():
    SummaryMessage = f"\n-----------------------------\n"
    SummaryMessage += f" # Summary Message #"
    SummaryMessage += f"\n- Generated At : {time.ctime()}"
    SummaryMessage += f"\n-----------------------------"
    SummaryMessage += f"\n+ Total Revenue : {get_TotalRevenue()} SAR"
    SummaryMessage += f"\n+ TotalOrders : {get_TotalOrders()} Orders"
    SummaryMessage += f"\n+ Average Order Value : {get_avg_OrderValues()} SAR"
    SummaryMessage += f"\n+ Average Rating : {avr_rating()}"
    SummaryMessage += f"\n+ Top Payment : {get_mostUsed_paymentTitle()} {percent_payment()}%"
    SummaryMessage += f"\n-----------------------------"

    return SummaryMessage


def staff_Performance():
    data = get_Staff()
    staffMessage = (f"\n-----------------------------"
                    f"\n Staff Performance"
                    f"\nGenerated At : {time.ctime()}"
                    f"\n-----------------------------"
                    f"\n+ TOP STAFF : {data[0][0]} -> {data[0][1]} times\n")
    for i in range(len(data)):
        staffMessage += f"\n* {data[i][0]} -> {data[i][1]} times"

    return staffMessage


def Days_Report():
    data = Analysis_Days(7)
    DaysA_Message = (f"\n-----------------------------"
                     f"\n Days_Report"
                     f"\n Generated At : {time.ctime()}"
                     f"\n-----------------------------"
                     f"\n+ TOP DAY : {data[0][0]} -> {data[0][1]} times\n")
    for i in range(len(data)):
        DaysA_Message += f"\n* {data[i][0]} -> {data[i][1]} times"
    return DaysA_Message


def OrderReport():
    data = Read_Data()
    low_ratings = data[data["customer_rating"] < 3]

    AlterMessage = (f"\n----------------------------"
                    f"\n Order Report "
                    f"\nGenerated At : {time.ctime()}")
    if low_ratings.empty:
        AlterMessage += "\n+ All items have good ratings!"
    else:
        # تحويل البيانات إلى قيم
        low_values = low_ratings.values
        AlterMessage += (f"\n- Found {len(low_values)} low rated orders (< 3 stars):"
                         f"\n----------------------------\n")
        for i in range(len(low_values)):
            # استخدمنا خيار تجليب اسم العمود مباشرة للحصول على الفهرس الصحيح تلقائياً
            item_name = low_ratings["item_name"].values[i]
            rating = low_ratings["customer_rating"].values[i]

            AlterMessage += (f"* Item {item_name} -> {int(rating)} Stars\n")
    return AlterMessage



