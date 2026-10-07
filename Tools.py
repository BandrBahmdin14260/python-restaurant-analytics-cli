import pandas as pd
import time

<<<<<<< HEAD
=======
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel

console = Console(force_terminal=True)

>>>>>>> cc18c47 (Add UI and colors using Rich)

def Read_Data():
    data = pd.read_csv("restaurant_data_large.csv")
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

<<<<<<< HEAD
    # 1. الترويسة وعدد الأسطر والأعمدة
    output = (
        f"\n----------------------------------------\n"
        f"         DATASET STRUCTURE OVERVIEW   \n"
        f"----------------------------------------\n"
        f"+ Total Records (Rows) : {len(data)}\n"
        f"+ Total Features (Cols): {len(data.columns)}\n"
        f"----------------------------------------\n"
        f"{'Column Name':<20} | {'Type':<10} \n"
        f"----------------------------------------\n"
=======
    table = Table(title="DATASET STRUCTURE OVERVIEW", box=box.ROUNDED, border_style="cyan")
    table.add_column("Column Name", style="bold white", justify="left")
    table.add_column("Type", style="yellow", justify="center")

    for col_name in data.columns:
        table.add_row(col_name, str(data[col_name].dtype))

    stats_panel = Panel(
        f"[bold cyan]Total Records (Rows):[/bold cyan] [white]{len(data)}[/white]\n"
        f"[bold cyan]Total Features (Cols):[/bold cyan] [white]{len(data.columns)}[/white]",
        border_style="cyan",
        expand=False
>>>>>>> cc18c47 (Add UI and colors using Rich)
    )

    console.print("\n")
    console.print(stats_panel)
    console.print(table)
    return ""


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
    if not Order:
        Order = input("Enter Order ID: ")
    if searchOrder(Order):
        data = Read_Data()
        matching_rows = data[data["order_id"] == Order].iloc[0]

        card_text = (
            f"[bold cyan]Branch      :[/bold cyan] [white]{matching_rows['branch']}[/white]\n"
            f"[bold cyan]Date        :[/bold cyan] [white]{matching_rows['order_date']}[/white]\n"
            f"[bold cyan]Time        :[/bold cyan] [white]{matching_rows['order_time']}[/white]\n"
            f"[bold cyan]Day         :[/bold cyan] [white]{matching_rows['day_of_week']}[/white]\n"
            f"[bold cyan]Order Type  :[/bold cyan] [white]{matching_rows['order_type']}[/white]\n"
            f"----------------------------------------\n"
            f"[bold yellow]Item        :[/bold yellow] [white]{matching_rows['item_name']} (x{matching_rows['quantity']})[/white]\n"
            f"[bold yellow]Payment     :[/bold yellow] [white]{matching_rows['payment_method']}[/white]\n"
            f"[bold yellow]Net Amount  :[/bold yellow] [bold green]{matching_rows['net_amount_sar']} SAR[/bold green]\n"
            f"----------------------------------------\n"
            f"[bold cyan]Staff Name  :[/bold cyan] [white]{matching_rows['staff_name']}[/white]"
        )

        panel = Panel(
            card_text,
            title=f"[bold cyan]ORDER CARD: {matching_rows['order_id']}[/bold cyan]",
            border_style="cyan",
            expand=False
        )
        console.print("\n")
        console.print(panel)
        return ""
    else:
        console.print("\n[bold red]Order Not Found![/bold red]")
        return ""


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

    branch_table = Table(title="Branch Performance", box=box.ROUNDED, border_style="cyan")
    branch_table.add_column("Metric", style="cyan")
    branch_table.add_column("Details", style="bold white")
    branch_table.add_row("Top Branch", f"{Branch['max'][1]} ({Branch['max'][0]} orders)")
    branch_table.add_row("Lowest Branch", f"{Branch['min'][1]} ({Branch['min'][0]} orders)")
    branch_table.add_row("Average Orders", f"{Branch['mean']}")

    time_table = Table(title="Top Peak Hours", box=box.ROUNDED, border_style="cyan")
    time_table.add_column("Time Slot", style="yellow")
    time_table.add_column("Orders Count", style="bold white")
    for t, count in TimeList:
        time_table.add_row(str(t), f"{count} times")

    item_table = Table(title="Top Popular Items", box=box.ROUNDED, border_style="cyan")
    item_table.add_column("Item Name", style="yellow")
    item_table.add_column("Orders Count", style="bold white")
    for item, count in BestOrders:
        item_table.add_row(str(item), f"{count} times")

    console.print("\n")
    console.print(
        Panel("[bold cyan]BRANCH & PEAK TIME REPORT[/bold cyan]", border_style="cyan", expand=False))
    console.print(branch_table)
    console.print(time_table)
    console.print(item_table)
    return ""


def Summary_Data():
    summary_text = (
        f"[bold dim]Generated At : {time.ctime()}[/bold dim]\n"
        f"----------------------------------------\n"
        f"[bold cyan] Total Revenue       :[/bold cyan] [bold green]{get_TotalRevenue():,.2f} SAR[/bold green]\n"
        f"[bold cyan] Total Orders        :[/bold cyan] [white]{get_TotalOrders()} Orders[/white]\n"
        f"[bold cyan] Average Order Value :[/bold cyan] [white]{get_avg_OrderValues():,.2f} SAR[/white]\n"
        f"[bold yellow] Average Rating      :[/bold yellow] [white]{avr_rating():.2f}[/white]\n"
        f"[bold yellow] Top Payment Method  :[/bold yellow] [white]{get_mostUsed_paymentTitle()} ({percent_payment()}%)[/white]"
    )

    panel = Panel(
        summary_text,
        title="[bold cyan]EXECUTIVE SUMMARY REPORT[/bold cyan]",
        border_style="cyan",
        expand=False
    )
    console.print("\n")
    console.print(panel)
    return ""


def staff_Performance():
    data = get_Staff()

    table = Table(title=f"Staff Performance\n[dim]Generated At : {time.ctime()}[/dim]", box=box.ROUNDED,
                  border_style="cyan")
    table.add_column("Rank", justify="center", style="yellow")
    table.add_column("Staff Name", style="bold white")
    table.add_column("Completed Orders", justify="center", style="green")

    for i, (name, count) in enumerate(data, start=1):
        rank = f"#{i}"
        table.add_row(rank, name, f"{count} times")

    console.print("\n")
    console.print(table)
    return ""


def Days_Report():
    data = Analysis_Days(7)

    table = Table(title=f"Days Activity Report\n[dim]Generated At : {time.ctime()}[/dim]", box=box.ROUNDED,
                  border_style="cyan")
    table.add_column("Day", style="bold yellow")
    table.add_column("Total Orders", justify="center", style="bold white")

    for day, count in data:
        table.add_row(day, f"{count} orders")

    console.print("\n")
    console.print(table)
    return ""


def OrderReport():
    data = Read_Data()
    low_ratings = data[data["customer_rating"] < 3]

    if low_ratings.empty:
        console.print("\n[bold green]All items have good ratings![/bold green]")
    else:
        table = Table(title=f"Low Rated Orders Report (< 3 Stars)\n[dim]Generated At : {time.ctime()}[/dim]",
                      box=box.ROUNDED, border_style="cyan")
        table.add_column("Item Name", style="bold white")
        table.add_column("Customer Rating", justify="center", style="yellow")

        for i in range(len(low_ratings)):
            item_name = low_ratings["item_name"].values[i]
            rating = low_ratings["customer_rating"].values[i]
            table.add_row(str(item_name), f"{int(rating)} Stars")

        console.print("\n")
        console.print(table)
    return ""