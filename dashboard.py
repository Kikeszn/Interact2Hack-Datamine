import streamlit as st
import pandas as pd
import numpy as np

# Configuración de página: debe ser la primera instrucción de Streamlit
st.set_page_config(page_title="Interact2Hack Dashboard", layout="wide")

def main():
    st.title("🚀 Interact2Hack Datamine Dashboard")
    st.markdown("---")

    # 1. Prueba de carga (Para descartar que sea tu lógica la que falla)
    st.sidebar.header("Filtros")
    data_option = st.sidebar.selectbox("Seleccionar dataset", ["Datos A", "Datos B"])

    # 2. Área de visualización
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Visualización Principal")
        # Generamos datos de prueba para asegurar que el dashboard no se vea negro
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
        st.line_chart(chart_data)

    with col2:
        st.subheader("Estado del Sistema")
        st.success("El dashboard está conectado y funcionando.")
        st.write(f"Visualizando: {data_option}")

    
if __name__ == "__main__":
    main()
