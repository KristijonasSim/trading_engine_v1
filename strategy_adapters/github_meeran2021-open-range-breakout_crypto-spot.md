# Strategy adapter: meeran2021

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/meeran2021/Open-Range-Breakout
- Source market: `stocks`
- Author: meeran2021
- Summary: Open Range Breakout: India stock market opens at 9:15 am and close at 3:30pm. We need to check for results for open range breakout trade in Banknifty for 1st 15 mins. We will buy Banknifty if 1st 15 min (9:15-9:30am) high is crossed or sell if 1st 15 min low is crossed with 0.5% as stop loss. Maximum 1 trade per day will be taken (this means that if the high of 1st 15 min is crossed first and a buy position is initiated, we will not initiate the sell trade and vice versa). If stop loss is not hit by 3:15pm, square off the position at 3:15pm. If you have problem understanding the strategy, you can search for “open range breakout trading strategy” online. You need to come out with the Profit and loss account for 2020 trading the above strategy. You can download data for BANKNIFTY for 2020 from https://tradecatcher.blogspot.com/p/ieod-data.html .

## Original rules

- Entry: `unknown`
- Exit: `unknown`
- Stop loss: `unknown`
- Position size: `unknown`

## Crypto adaptation

- Pairs: `unknown`
- Timeframe: `unknown`
- Session or UTC time: `unknown`
- Long / short rule: `unknown`
- Fee and slippage: `unknown`
- What changed from original: `unknown`

## Approval

- Reviewer:
- Decision: `needs work`
- Ready for Testing Engine: `no`

## Automation

- Result: Claude reviewed the public source; proposed breakout rules: EMA 11/44, RSI entry > 55, exit < 44, stop-loss -5%, fixed $100 position, 15m. Testing must judge it; it is not claimed as the original author's exact strategy.
