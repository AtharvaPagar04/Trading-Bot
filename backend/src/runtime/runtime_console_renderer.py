def render_runtime_snapshot(
    snapshot,
):

    runtime = (
        snapshot["runtime"]
    )

    telemetry = (
        snapshot["telemetry"]
    )

    portfolio = (
        snapshot["portfolio"]
    )

    trade_journal = (
        snapshot["trade_journal"]
    )
    active_trades = (
        snapshot["active_trades"]
    )


    print()

    print(
        "=" * 50
    )

    print(
        "RUNTIME STATUS"
    )

    print(
        "=" * 50
    )

    print(
        f"Operating State : "
        f"{runtime['operating_state']}"
    )

    print(
        f"Safe Mode       : "
        f"{runtime['safe_mode']}"
    )

    print()

    print(
        "=" * 50
    )

    print(
        "MARKET TELEMETRY"
    )

    print(
        "=" * 50
    )

    print(
        f"Latest Price    : "
        f"{telemetry['latest_price']}"
    )

    print(
        f"Latest Candle   : "
        f"{telemetry['latest_candle_close']}"
    )

    print(
        f"Total Trades    : "
        f"{telemetry['total_trades']}"
    )
    print(
        f"Unrealized PnL : "
        f"{telemetry['current_unrealized_pnl']}"
    )

    print(
        f"PnL Percent    : "
        f"{telemetry['current_unrealized_pnl_percent']:.4f}%"
    )

    print(
        f"Last Execution  : "
        f"{telemetry['last_execution_time']}"
    )

    print()

    print(
        "=" * 50
    )

    print(
        "PORTFOLIO"
    )

    print(
        "=" * 50
    )

    print(
        f"Total Capital   : "
        f"{portfolio['total_capital']}"
    )

    print(
        f"Available Cash  : "
        f"{portfolio['available_capital']}"
    )
    
    print(
        f"Invested Capital: "
        f"{portfolio['invested_capital']}"
    )

    print(
        f"Holdings Value  : "
        f"{portfolio['holdings_value']}"
    )

    print(
        f"Unrealized PnL  : "
        f"{portfolio['total_unrealized_pnl']}"
    )

    print(
        f"Portfolio Value : "
        f"{portfolio['total_portfolio_value']}"
    )

    print()

    print(
        "ACTIVE TRADES"
    )

    print()

    if not active_trades:
        print(
            "No Active Trades"
        )
    else:

        for trade in active_trades:

            print(
                f"- "
                f"{trade['symbol']} | "
                f"Status="
                f"{trade['status']} | "
                f"Qty="
                f"{trade['quantity']} | "
                f"Entry="
                f"{trade['entry_price']} | "
                f"Current="
                f"{trade['current_price']} | "
                f"PnL="
                f"{trade['unrealized_pnl']:.4f} | "
                f"PnL%="
                f"{trade['unrealized_pnl_percent']:.4f}%"
            )

    if (
        not portfolio["positions"]
    ):

        print(
            "No Open Positions"
        )

    else:

        for position in (
            portfolio["positions"]
        ):

            print(
                f"- "
                f"{position['symbol']} | "
                f"Qty="
                f"{position['quantity']} | "
                f"Avg="
                f"{position['average_price']}"
            )

    print()

    print(
        "RECENT TRADES"
    )

    print()

    if not trade_journal:

        print(
            "No Completed Trades"
        )

    else:

        recent_trades = (
            trade_journal[-5:]
        )

        for trade in recent_trades:

            print(
                f"- "
                f"{trade['symbol']} | "
                f"PnL="
                f"{trade['realized_pnl']} | "
                f"Fees="
                f"{trade['fees_paid']}"
            )

    print()
    print(
        "=" * 50
    )

    print()