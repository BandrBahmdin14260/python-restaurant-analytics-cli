from Tools import *
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel

console = Console(force_terminal=True)

panel = Panel(
    "[bold white] Welcome to Python Restaurant System[/bold white]\n"
    "[dim]Select an option from the menu to proceed.[/dim]",
    title="[bold green]MAIN MENU[/bold green]",
    border_style="bright_blue",
    padding=(1, 2)
)

console.print(panel)

# 2. إنشاء جدول الخيارات
table = Table(title="Restaurant Menu Options", box=box.DOUBLE, style="magenta")

table.add_column("Option", justify="center", style="cyan", no_wrap=True)
table.add_column("Description", style="white")

table.add_row("[white]1", "Information about Data")
table.add_row("[white]2", "Executive Summary Method")
table.add_row("[white]3", "Peak Time and Branch Method")
table.add_row("[white]4", "Search Order Information")
table.add_row("[white]5", "Staff Report")
table.add_row("[white]6", "Days Report")
table.add_row("[white]7", "Manager Alerts (Low Rating)")
table.add_row("[white]0", "Exit")

console.print(table)


while True:
    userInput = input("\nEnter a number: ").strip()

    match userInput:
        case "1":
<<<<<<< HEAD
            print(columns_Data())
        case "2":
            print(Summary_Data())
        case "3":
            print(PeakTime_Branch())
        case "4":
            Order = input("Enter Order Number: ").strip()
            print(Order_Info(Order))
        case "5":
            print(staff_Performance())
        case "6":
            print(Days_Report())
        case "7":
            print(OrderReport())
        case "0":
            print("Bye.. ")
            break
        case _:
            print("\n⚠️ Invalid selection! Please enter a valid number from 0 to 7.")
            print(Welcome_Message)
=======
            console.print(columns_Data())
        case "2":
            console.print(Summary_Data())
        case "3":
            console.print(PeakTime_Branch())
        case "4":
            Order = input("Enter Order Number: ").strip()
            console.print(Order_Info(Order))
        case "5":
            console.print(staff_Performance())
        case "6":
            console.print(Days_Report())
        case "7":
            console.print(OrderReport())
        case "0":
            console.print("[bold red]Bye..[/bold red]")
            break
        case _:
            console.print("\n[bold red] Invalid selection! Please enter a valid number from 0 to 7.[/bold red]")
            console.print(table)
>>>>>>> cc18c47 (Add UI and colors using Rich)
