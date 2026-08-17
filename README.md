# trading_engine_v1

See [ROADMAP.md](ROADMAP.md) for the planned automatic-trading workflow.

Research Engine v1 is in [research_engine/README.md](research_engine/README.md).

Run the local dashboard with `python3 -m ui`. See [ui/README.md](ui/README.md).

Testing Engine decision: [TESTING_SUITE_DECISION.md](TESTING_SUITE_DECISION.md).

The Strategy Adapter can use a locally signed-in Claude Code client to classify
public source text into a source-specific BTC test hypothesis. No LLM API key is
stored in this repository; if the client is unavailable, diversified local rule
templates remain available.
