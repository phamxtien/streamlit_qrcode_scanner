import base64
from io import BytesIO
from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called camera_input_live,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "qrcode_scanner", path=str(frontend_dir)
)


def qrcode_scanner(key: Optional[str] = None) -> Optional[BytesIO]:
    """
    Add a descriptive docstring
    """
    data: Optional[str] = _component_func(key=key)

    if data is None:
        return None

    # raw_data = b64_data.split(",")[1]  # Strip the data: type prefix

    # component_value = BytesIO(base64.b64decode(raw_data))
    component_value = data

    return component_value


def main():
    st.write("## Example")

    image = qrcode_scanner()

    if image is not None:
        st.image(image)


if __name__ == "__main__":
    main()
