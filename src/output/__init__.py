from src.output.json_output import JSONOutput

OUTPUT_FORMATTERS = {
    "json": JSONOutput,
    # "txt": TextOutput,  # ← здесь можно регистрировать новые форматы
}
