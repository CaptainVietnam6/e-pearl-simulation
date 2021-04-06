from random import randint

trade_list = []
run_num = 0
successful_trades = 0
successful_trades_list = []

while len(trade_list) < 42:
    trade_list.clear()
    successful_trades = 0
    for i in range(262):
        trade_rng = randint(1,10000)
        if trade_rng <= 442:
            trade_list.append(trade_rng)
            trade_list.sort()
            successful_trades = successful_trades + 1
            successful_trades_list.append(successful_trades)
            successful_trades_list.sort()

    run_num = run_num + 1
    print("On run " + str(run_num) + " there were " + str(len(trade_list)) + "/262" + " successful pearl trades")
    print("The highest amount of successful pearl trades so far is " + str(max(successful_trades_list)))
    print("\n")
    