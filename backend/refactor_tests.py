import os
import glob
import re

TEST_DIR = '/home/arch/DEV/ML/grid-trading-bot-v3/backend/tests'

replace_pattern_1 = re.compile(
    r'runtime\s*=\s*GovernedRuntime\(\s*RuntimeMode\.DRY_RUN,\s*EventBus\(\),\s*\)'
)

replacement_1 = """runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)"""

replace_pattern_2 = re.compile(
    r'runtime\s*=\s*GovernedRuntime\(\s*mode\s*=\s*RuntimeMode\.DRY_RUN,\s*event_bus\s*=\s*bus,\s*\)'
)

replacement_2 = """runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=bus,
)"""

for root, _, files in os.walk(TEST_DIR):
    for filename in files:
        if filename.endswith('.py'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                content = f.read()

            original_content = content
            
            content = replace_pattern_1.sub(replacement_1, content)
            content = replace_pattern_2.sub(replacement_2, content)

            if content != original_content:
                # Need to add import
                if 'from src.core.runtime_builder import' not in content:
                    content = "from src.core.runtime_builder import (\n    build_runtime_state,\n)\n" + content
                
                # Check if RuntimeMode is still used
                if 'RuntimeMode' not in content.replace('from src.runtime.runtime_enums import (\n    RuntimeMode,\n)', '').replace('from src.runtime.runtime_enums import RuntimeMode', ''):
                    # It's no longer used
                    content = re.sub(r'from src\.runtime\.runtime_enums import \(\n\s*RuntimeMode,\n\)', '', content)
                    content = re.sub(r'from src\.runtime\.runtime_enums import \(\n\s*RuntimeMode,\s*\n\)', '', content)
                    content = re.sub(r'from src\.runtime\.runtime_enums import RuntimeMode\n', '', content)
                    content = re.sub(r',\n\s*RuntimeMode,\n', ',\n', content) # if part of multi-import

                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Updated {filepath}")
