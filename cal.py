Here are the **detailed, clean, exam-ready steps** for your Jenkins CI Pipeline (based on your PDF) 👇

---

# 🧾 ✅ JENKINS CI PIPELINE USING GIT & MAVEN – DETAILED STEPS

---

## 🔹 STEP 1: Create Maven Project (Folder Structure)

Create a project named **simple-maven-app** with proper Maven structure:

```
simple-maven-app/
 ├── pom.xml
 └── src/
     ├── main/java/com/example/App.java
     └── test/java/com/example/AppTest.java
```

✔ This structure is **mandatory** for Maven to work correctly 

---

## 🔹 STEP 2: Create Main Java File (App.java)

📁 Path:

```
src/main/java/com/example/App.java
```

👉 Code:

```java
package com.example;

public class App {
    public int add(int a, int b) {
        return a + b;
    }
}
```

✔ This contains the **business logic** (addition function) 

---

## 🔹 STEP 3: Create Test File (AppTest.java)

📁 Path:

```
src/test/java/com/example/AppTest.java
```

👉 Code:

```java
package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test
    public void testAdd() {
        App app = new App();
        assertEquals(5, app.add(2, 3));
    }
}
```

✔ Uses **JUnit testing**
✔ If test fails → build fails 

---

## 🔹 STEP 4: Create pom.xml (Project Configuration)

📁 Path:

```
simple-maven-app/pom.xml
```

👉 Important content:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>simple-maven-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

✔ Defines:

* Project details
* Dependencies (JUnit) 

---

## 🔹 STEP 5: Test Project Locally

👉 Run command:

```
mvn clean test
```

✔ Expected Output:

```
BUILD SUCCESS
```

✔ Confirms project works before CI 

---

## 🔹 STEP 6: Push Project to GitHub

👉 Commands:

```
git init
git add .
git commit -m "Initial Maven project"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

✔ Uploads code to GitHub for Jenkins access 

---

## 🔹 STEP 7: Install Maven (Windows)

1. Download Maven ZIP
2. Extract to:

   ```
   C:\Program Files\Apache\apache-maven-3.9.12
   ```
3. Set Environment Variable:

   ```
   MAVEN_HOME = C:\Program Files\Apache\apache-maven-3.9.12
   ```
4. Add to PATH:

   ```
   %MAVEN_HOME%\bin
   ```
5. Verify:

   ```
   mvn -version
   ```

✔ Confirms Maven installed correctly 

---

## 🔹 STEP 8: Configure Maven in Jenkins

📍 Go to:

```
Manage Jenkins → Tools → Maven Installations
```

👉 Set:

* Name: `M3`
* MAVEN_HOME: (same path as above)
* Uncheck **Install Automatically**

✔ Links Maven with Jenkins 

---

## 🔹 STEP 9: Create Jenkins Pipeline Script

👉 Add this pipeline code:

```groovy
pipeline {
    agent any

    tools {
        maven 'M3'
    }

    stages {
        stage('Checkout Git') {
            steps {
                git branch: 'main',
                url: '<your-repository-url>'
            }
        }

        stage('Build and Test') {
            steps {
                bat 'mvn clean test'
            }
        }
    }
}
```

✔ Stages:

* Checkout code
* Build + Test 

---

## 🔹 STEP 10: Run Pipeline in Jenkins

👉 Steps:

1. Save pipeline
2. Click **Build Now**
3. Open **Console Output**

✔ Expected Result:

* Tests executed
* BUILD SUCCESS
* Finished: SUCCESS 

---

# 🎯 FINAL RESULT

✔ Jenkins will:

* Fetch code from GitHub
* Build using Maven
* Run JUnit tests
* Show SUCCESS / FAILURE automatically

---

If you want, I can also give you:
✅ Viva questions
✅ Diagram for this pipeline
✅ Short 5-mark answer version

Just tell me 👍


Here are the **detailed, step-by-step explanations** for all the Pipeline Tasks from your second PDF 👇

---

# 🧾 ✅ PIPELINE TASKS – DETAILED STEPS

---

## 🔹 ✅ **Pipeline Task 1 – Checkout Code + Show Files**

### 📌 Purpose:

* Fetch code from GitHub
* Display all files in workspace

### 🧩 Steps:

1. Jenkins starts the pipeline

2. Uses `agent any` → runs on any available node

3. Enters **Checkout Code stage**

4. Executes:

   ```groovy
   git 'https://github.com/your-username/your-repo.git'
   ```

   ✔ Downloads repository to Jenkins workspace

5. Moves to **Show Files stage**

6. Executes:

   ```groovy
   bat 'dir'
   ```

   ✔ Lists all files and folders

### 🎯 Output:

* All repo files visible in console

✔ Useful for verifying checkout 

---

## 🔹 ✅ **Pipeline Task 2 – Checkout + Print Directory Path**

### 📌 Purpose:

* Verify current working directory

### 🧩 Steps:

1. Pipeline starts
2. Checkout code from GitHub
3. Enters **Print Directory stage**
4. Runs:

   ```groovy
   bat 'cd'
   ```

   ✔ Displays current directory path

### 🎯 Output:

* Shows Jenkins workspace path

✔ Helps understand where code is stored 

---

## 🔹 ✅ **Pipeline Task 3 – Print Message**

### 📌 Purpose:

* Display custom message in pipeline

### 🧩 Steps:

1. Pipeline starts
2. Checkout code
3. Enters **Print Message stage**
4. Executes:

   ```groovy
   echo 'Hello! Jenkins Pipeline executed successfully'
   ```

### 🎯 Output:

* Message printed in console

✔ Used for debugging or confirmation messages 

---

## 🔹 ✅ **Pipeline Task 4 – Create File**

### 📌 Purpose:

* Create a new file using Jenkins

### 🧩 Steps:

1. Pipeline starts
2. Checkout code
3. Enters **Create File stage**
4. Executes:

   ```groovy
   bat 'echo This file is created by Jenkins > demo.txt'
   ```

   ✔ Creates file `demo.txt`

### 🎯 Output:

* File created inside workspace

✔ Demonstrates file creation automation 

---

## 🔹 ✅ **Pipeline Task 5 – Read File**

### 📌 Purpose:

* Read contents of a file

### 🧩 Steps:

1. Pipeline starts
2. Checkout code
3. Enters **Read File stage**
4. Executes:

   ```groovy
   bat 'type README.md'
   ```

   ✔ Displays content of README.md

### 🎯 Output:

* File content shown in console

✔ Useful for validation or logs 

---

# 🎯 FINAL UNDERSTANDING

All tasks follow same structure:

✔ Checkout code
✔ Perform one operation
✔ Show output in console

---

# ✨ QUICK SUMMARY (EXAM REVISION)

| Task   | Action         |
| ------ | -------------- |
| Task 1 | Show files     |
| Task 2 | Show directory |
| Task 3 | Print message  |
| Task 4 | Create file    |
| Task 5 | Read file      |

---

If you want next:
✅ Combined pipeline (all tasks in one)
✅ Viva questions + answers
✅ Diagram for pipeline flow

Just tell me 👍

Here are the **detailed, exam-ready steps** for your **Jenkins Pipeline with Parameters (Addition of Two Numbers – Python + BAT)** 👇

---
# 🧾 ✅ JENKINS PIPELINE WITH PARAMETERS – DETAILED STEPS

---

## 🔹 ✅ STEP 1: Create Python Script (add.py)

📁 Create a file named **add.py**

👉 Code:

```python
import sys

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    result = add_numbers(num1, num2)

    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum : {result}")
```

### 📌 Explanation:

1. `sys.argv` → takes input from command line
2. Converts input into integers
3. Calls function to add numbers
4. Prints formatted result

✔ This script performs addition dynamically 

---

## 🔹 ✅ STEP 2: Create Jenkins Pipeline Script

👉 Add this pipeline in Jenkins:

```groovy
pipeline {
    agent any

    parameters {
        string(name: 'BRANCH_NAME',
               defaultValue: 'main',
               description: 'Git branch')

        string(name: 'NUM1',
               defaultValue: '10',
               description: 'First Number')

        string(name: 'NUM2',
               defaultValue: '20',
               description: 'Second Number')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${params.BRANCH_NAME}",
                    url: 'https://github.com/Ramlingams/pipeline-parameters.git'
            }
        }

        stage('Addition Build') {
            steps {
                bat "python add.py ${params.NUM1} ${params.NUM2}"
            }
        }
    }
}
```

---

## 🔹 ✅ STEP 3: Understand Pipeline Flow

### 📌 How it works:

1. **agent any**
   → Runs pipeline on any available machine

2. **parameters block**
   → Creates input fields in Jenkins UI:

   * BRANCH_NAME
   * NUM1
   * NUM2

3. **Checkout Stage**

   * Fetches code from GitHub repository

4. **Addition Build Stage**

   * Runs Python script
   * Passes NUM1 and NUM2 as arguments

✔ Inputs are taken dynamically from user 

---

## 🔹 ✅ STEP 4: Run the Pipeline

### 🧩 Steps:

1. Save pipeline in Jenkins
2. Click **“Build with Parameters”**
3. Enter values:

   * NUM1 → (e.g., 5)
   * NUM2 → (e.g., 7)
4. Click **Build**
5. Open **Console Output**

---

## 🔹 ✅ STEP 5: Expected Output

```text
=================================
Addition Result
=================================
First Number : 5
Second Number: 7
Sum : 12
```

✔ Shows correct addition result

---

# 🎯 FINAL RESULT

✔ Jenkins:

* Accepts user input
* Fetches code
* Executes Python script
* Displays result

✔ Demonstrates **parameterized CI pipeline**

---

# ✨ QUICK EXAM SUMMARY

* Uses **parameters block**
* Takes user input dynamically
* Executes Python script via `bat`
* Displays result in console

---

If you want next:
✅ Viva questions from this
✅ 5-mark short answer
✅ Diagram (easy to draw in exam)

Just tell me 👍

Here are your **full detailed steps (experiment-wise, version-wise)** from the uploaded file 👇 — written in a clean, **exam + lab record format**

---

# 🧾 ✅ JENKINS PIPELINE EXPERIMENTS – DETAILED STEPS

---

# 🔥 ✅ EXPERIMENT 1: Basic Pipeline with Parameter & BAT

## 🎯 Objective:

To verify GitHub integration, parameters, and BAT command execution 

---

## 🔹 Version 1 Steps

1. Start Jenkins pipeline
2. Add **string parameter MESSAGE**
3. Checkout code from GitHub:

   ```groovy
   git 'repo-url'
   ```
4. Print parameter:

   ```groovy
   echo "${params.MESSAGE}"
   ```
5. Execute BAT command:

   ```groovy
   bat 'echo Hello from Jenkins'
   ```

---

## 🔹 Version 2 Steps

1. Modify file in GitHub
2. Pipeline fetches updated code
3. Run BAT command:

   ```groovy
   bat 'date /t'
   ```
4. Print MESSAGE again

---

## 🔹 Version 3 Steps

1. Checkout latest commit
2. Create file:

   ```groovy
   bat 'echo Jenkins output > output.txt'
   ```
3. Display file:

   ```groovy
   bat 'type output.txt'
   ```

---

## 🔹 Version 4 Steps

1. Add parameter: USERNAME
2. Checkout repo
3. Create file:

   ```groovy
   bat 'echo %USERNAME% > user.txt'
   ```

---

# 🔥 ✅ EXPERIMENT 2: Boolean & Choice Parameters

## 🎯 Objective:

Understand different parameter types 

---

## 🔹 Version 1 (Boolean)

1. Add parameter:

   ```groovy
   booleanParam(name: 'RUN_TEST')
   ```
2. If true:

   ```groovy
   if (params.RUN_TEST) {
       bat 'echo Running Test'
   }
   ```

---

## 🔹 Version 2 (Choice)

1. Add:

   ```groovy
   choice(name: 'ENV', choices: ['DEV','TEST','PROD'])
   ```
2. Print:

   ```groovy
   echo "${params.ENV}"
   ```

---

## 🔹 Version 3 (String)

1. Add BUILD_NAME parameter
2. Create file:

   ```groovy
   bat 'echo %BUILD_NAME% > build.txt'
   ```

---

## 🔹 Version 4 Steps

1. Print workspace:

   ```groovy
   bat 'echo %WORKSPACE%'
   ```
2. Print all parameters

---

# 🔥 ✅ EXPERIMENT 3: Build Simulation

## 🎯 Objective:

Simulate build without Maven 

---

## 🔹 Version 1

```groovy
bat 'echo Compiling...'
bat 'echo Build Successful'
```

---

## 🔹 Version 2

```groovy
bat 'mkdir build'
bat 'copy * build'
```

---

## 🔹 Version 3

```groovy
bat 'dir'
bat 'echo %DATE% %TIME%'
```

---

## 🔹 Version 4

```groovy
bat 'echo artifact > artifact.txt'
archiveArtifacts 'artifact.txt'
```

---

# 🔥 ✅ EXPERIMENT 4: Manual Input & Approval

## 🎯 Objective:

Implement approval system 

---

## 🔹 Version 1

```groovy
input 'Proceed with Build?'
echo 'Approved'
```

---

## 🔹 Version 2

1. Accept input during execution
2. Display approval:

```groovy
bat 'echo Approved'
```

---

## 🔹 Version 3

```groovy
echo "${env.BUILD_NUMBER}"
echo "Build running"
```

---

## 🔹 Version 4

```groovy
bat 'echo %PARAM% > file.txt'
```

---

# 🔥 ✅ EXPERIMENT 5: File Handling

## 🎯 Objective:

Perform file operations 

---

## 🔹 Version 1

```groovy
bat 'echo Sample > sample.txt'
bat 'type sample.txt'
```

---

## 🔹 Version 2

```groovy
bat 'echo New Line >> sample.txt'
bat 'find /c /v "" sample.txt'
```

---

## 🔹 Version 3

```groovy
bat 'rename sample.txt newfile.txt'
bat 'dir'
```

---

## 🔹 Version 4

```groovy
bat 'del newfile.txt'
bat 'dir'
```

---

# 🔥 ✅ EXPERIMENT 6: Environment Variables

## 🎯 Objective:

Use environment variables 

---

## 🔹 Version 1

```groovy
bat 'set'
bat 'echo Hello Jenkins'
```

---

## 🔹 Version 2

```groovy
environment {
    MY_VAR = 'Hello'
}
bat 'echo %MY_VAR%'
```

---

## 🔹 Version 3

```groovy
bat 'echo %VERSION% > version.txt'
```

---

## 🔹 Version 4

```groovy
bat 'git rev-parse HEAD'
echo "Build Completed"
```

---

# 🎯 FINAL SUMMARY

✔ All experiments include:

* GitHub checkout
* Parameter usage
* BAT command execution
* File handling
* Build simulation
* User input handling

---

If you want next (very useful 👇):
✅ **Full combined pipeline (all experiments in one)**
✅ **Important viva questions (very likely exam)**
✅ **Super short revision (1 page)**

Just tell me 👍

Here are the **detailed, clean steps** for your **Jenkins Maven Project (Without Archetype)** 👇

---
# 🧾 ✅ JENKINS MAVEN PROJECT – DETAILED STEPS

---

## 🔹 ✅ STEP 1: Install Required Software

Install the following:

1. Java Development Kit (JDK)
2. Apache Maven
3. Jenkins
4. Git

### ✔ Verify installation:

```bash
java -version
mvn -version
git --version
```

✔ Ensures all tools are properly installed 

---

## 🔹 ✅ STEP 2: Create Project Folder

1. Create a folder manually:

```
my_maven_project
```

✔ This is your project root directory 

---

## 🔹 ✅ STEP 3: Create Project Structure

Inside the folder, create:

```
my_maven_project/
 ├── pom.xml
 └── src/
     └── main/
         └── java/
             └── com/
                 └── example/
                     └── App.java
```

✔ Maven requires this standard structure 

---

## 🔹 ✅ STEP 4: Create pom.xml

📁 Path:

```
my_maven_project/pom.xml
```

👉 Code:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my_maven_project</artifactId>
    <version>1.0-SNAPSHOT</version>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### 📌 Explanation:

* Defines project details
* Configures Java compiler

✔ Required for Maven build 

---

## 🔹 ✅ STEP 5: Create Java File

📁 Path:

```
src/main/java/com/example/App.java
```

👉 Code:

```java
package com.example;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello Maven Jenkins Project");
    }
}
```

✔ Simple program to test build 

---

## 🔹 ✅ STEP 6: Build Project Locally

👉 Run:

```bash
mvn clean package
```

✔ Compiles code and creates JAR file

---

## 🔹 ✅ STEP 7: Check Build Output

Expected:

```
BUILD SUCCESS
```

📁 Output folder:

```
target/
 my_maven_project-1.0-SNAPSHOT.jar
```

✔ Confirms successful build 

---

## 🔹 ✅ STEP 8: Push Project to GitHub

👉 Commands:

```bash
git init
git add .
git commit -m "Maven Project"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

✔ Makes project accessible to Jenkins 

---

## 🔹 ✅ STEP 9: Open Jenkins

👉 Open browser:

```
http://localhost:8080
```

✔ Access Jenkins dashboard 

---

## 🔹 ✅ STEP 10: Configure Maven in Jenkins

📍 Go to:

```
Manage Jenkins → Global Tool Configuration
```

👉 Add:

* Name: Maven3
* Install automatically: ✅

✔ Links Maven with Jenkins 

---

## 🔹 ✅ STEP 11: Create Maven Job

1. Click **New Item**
2. Enter name: `MVN_01`
3. Select: **Maven Project**
4. Click OK

✔ Creates Jenkins job 

---

## 🔹 ✅ STEP 12: Configure GitHub Repository

👉 In Source Code Management:

* Select Git
* Enter Repository URL
* Branch:

```
*/main
```

✔ Connects Jenkins with GitHub 

---

## 🔹 ✅ STEP 13: Configure Build

👉 In Build section:

* Root POM:

```
pom.xml
```

* Goals:

```
clean package
```

✔ Defines build process 

---

## 🔹 ✅ STEP 14: Run Build

1. Click **Build Now**
2. Open **Console Output**

✔ Monitor execution

---

## 🔹 ✅ STEP 15: Final Output

✔ Expected:

```
BUILD SUCCESS
```

📁 Output file location:

```
workspace/MVN_01/target/my_maven_project-1.0-SNAPSHOT.jar
```

✔ JAR file successfully generated 

---

# 🎯 FINAL RESULT

✔ Jenkins:

* Fetches code from GitHub
* Builds project using Maven
* Generates JAR file
* Shows build status

---

# ✨ QUICK EXAM SUMMARY

* Create Maven project manually
* Configure pom.xml
* Push to GitHub
* Configure Jenkins job
* Run build → get JAR

---

If you want next:
✅ Viva questions (very important)
✅ 5-mark short answer
✅ Diagram for exam

Just tell me 👍

Here are your **detailed steps (Experiments 7–11)** in a clean **lab-record + exam format** 👇

---

# 🧾 ✅ JENKINS PIPELINE EXPERIMENTS (7–11) – DETAILED STEPS

---

# 🔥 ✅ EXPERIMENT 7: Workspace Information & Logging

## 🎯 Objective:

Understand workspace details and logging 

---

## 🔹 Version 1

1. Checkout code from GitHub
2. Display workspace path:

```groovy
bat 'echo %WORKSPACE%'
```

3. Print message:

```groovy
echo "Pipeline execution started"
```

---

## 🔹 Version 2

1. Checkout updated repo
2. List files:

```groovy
bat 'dir'
```

3. Display time:

```groovy
bat 'time /t'
```

---

## 🔹 Version 3

1. Checkout latest code
2. Create log file:

```groovy
bat 'echo Build started > buildlog.txt'
```

3. Display file:

```groovy
bat 'type buildlog.txt'
```

---

## 🔹 Version 4

1. Checkout repo
2. Append build number:

```groovy
bat 'echo %BUILD_NUMBER% >> buildlog.txt'
```

3. Display updated file

---

# 🔥 ✅ EXPERIMENT 8: Parameterized Pipeline

## 🎯 Objective:

Use parameters in pipeline 

---

## 🔹 Version 1

1. Add parameter:

```groovy
string(name: 'PROJECT_NAME')
```

2. Print:

```groovy
echo "${params.PROJECT_NAME}"
```

---

## 🔹 Version 2

1. Add numeric parameter BUILD_ID
2. Store in file:

```groovy
bat 'echo %BUILD_ID% > buildinfo.txt'
```

---

## 🔹 Version 3

1. Add parameters:

* APP_NAME
* VERSION

2. Print combined:

```groovy
echo "${params.APP_NAME} ${params.VERSION}"
```

---

## 🔹 Version 4

1. Print all parameters
2. Save to file:

```groovy
bat 'echo parameters saved > parameters.txt'
```

---

# 🔥 ✅ EXPERIMENT 9: Directory Operations

## 🎯 Objective:

Perform folder operations 

---

## 🔹 Version 1

```groovy
bat 'mkdir testfolder'
bat 'dir'
```

---

## 🔹 Version 2

```groovy
bat 'echo file1 > testfolder/file1.txt'
bat 'echo file2 > testfolder/file2.txt'
bat 'dir testfolder'
```

---

## 🔹 Version 3

```groovy
bat 'copy README.md testfolder'
bat 'dir testfolder'
```

---

## 🔹 Version 4

```groovy
bat 'rmdir /s /q testfolder'
bat 'dir'
```

---

# 🔥 ✅ EXPERIMENT 10: Build Metadata

## 🎯 Objective:

Display Jenkins build details 

---

## 🔹 Version 1

```groovy
echo "${env.BUILD_NUMBER}"
echo "${env.JOB_NAME}"
```

---

## 🔹 Version 2

```groovy
echo "${env.NODE_NAME}"
echo "${env.WORKSPACE}"
```

---

## 🔹 Version 3

```groovy
bat 'echo %BUILD_NUMBER% > buildinfo.txt'
bat 'echo %JOB_NAME% >> buildinfo.txt'
bat 'type buildinfo.txt'
```

---

## 🔹 Version 4

```groovy
bat 'echo %DATE% %TIME% >> buildinfo.txt'
bat 'type buildinfo.txt'
```

---

# 🔥 ✅ EXPERIMENT 11: Execution Messages & Status

## 🎯 Objective:

Show pipeline execution flow 

---

## 🔹 Version 1

```groovy
echo "Pipeline Started"
echo "Pipeline Completed"
```

---

## 🔹 Version 2

```groovy
echo "Processing files..."
echo "Processing complete"
```

---

## 🔹 Version 3

```groovy
bat 'echo Build Successful > status.txt'
```

---

## 🔹 Version 4

```groovy
bat 'echo Pipeline Execution Completed >> status.txt'
bat 'type status.txt'
```

---

# 🎯 FINAL SUMMARY (VERY IMPORTANT)

✔ These experiments cover:

* Workspace info
* Parameters
* File & directory operations
* Build metadata
* Execution messages

✔ All pipelines follow:
👉 Checkout → Process → Output

---

# ✨ SUPER SHORT REVISION

| Exp | Topic            |
| --- | ---------------- |
| 7   | Workspace & logs |
| 8   | Parameters       |
| 9   | Directory ops    |
| 10  | Build info       |
| 11  | Messages         |

---

If you want next (high scoring 👇):
✅ **Full lab record (ready to write)**
✅ **Viva questions (very expected)**
✅ **All experiments combined pipeline**

Just tell me 👍
