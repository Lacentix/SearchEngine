## Setting Up Java Environment for Flask Application

To run the Flask application that requires a Java environment (e.g., for PyTerrier integration), follow these steps to configure `JAVA_HOME` and use the updated code:

### 1. Set `JAVA_HOME` Environment Variable

Ensure that `JAVA_HOME` is properly configured on your system:

- **Linux/macOS**:
  Open a terminal and set `JAVA_HOME` by exporting the path to your Java installation directory. For example:
  ```bash
  export JAVA_HOME=/path/to/java/home

## Running the Flask Application
`flask run --host 0.0.0.0 --port 8000 --debugger`