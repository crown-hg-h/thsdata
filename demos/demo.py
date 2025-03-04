from thsdata import Quote, FuquanNo
import datetime


def main():
    # 初始化
    quote = Quote()

    try:
        # quote.connect()
        start_date = datetime.datetime(2024, 1, 1)
        end_date = datetime.datetime(2025, 2, 28)
        data = quote.security_bars_daily("USHA600519", start_date, end_date, FuquanNo)
        print(data)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # 断开连接
        quote.disconnect()
        print("Disconnected from the server.")


if __name__ == "__main__":
    main()
