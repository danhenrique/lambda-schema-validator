# lambda-schema-validator

## Generating the zip on terminal with zip

1. Go inside the `app` folder in terminal

    ```bash
    cd app
    ```

2. Create a folder to store all dependencies that are needed to run the python code. For example a folder with `package` name.

    ```bash
    mkdir package
    ```

3. Run the command below to store all files from dependencies

    ```bash
    pip install -r requirements.txt --target ./package
    ```

4. Zip all dependencies inside a file in the root directory

    ```bash
    cd package
    zip -r ../dist/app.zip .
    cd ..
    ```

5. If needed, also zip all custom modules that are inside other folders, like `src`

    ```bash
    zip -r dist/app.zip ./src
    ```

6. Finally, add the file with the handler to the root of the zip file

    ```bash
    zip dist/app.zip lambda_function.py
    ```
