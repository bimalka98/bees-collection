# *Creating a virtual environment for Computer Vision*
> ***Note:: If you plan to use TensorFlow 2, please install a Python version compatible with*** [Tensorflow](https://www.tensorflow.org/install)

Complete video guide can be found [here](https://youtu.be/xE8w6OQzf8w).

Following steps describe only the creation of virtual environments.

1. Open command Prompt and follow the steps.

2. Change the Directory to: `C:\Python39`

3. Upgrade pip: `python -m pip install --upgrade pip`

4. Install `virtualenv` package: `python -m pip install virtualenv`

5. Create virtual environment: `virtualenv cv`

6. Change the directory to: `C:\Python39\cv\Scripts`

7. Activate the cv environment: `activate cv`

8. Then install the required packages

```shell
pip install numpy
pip install matplotlib
pip install opencv-python
pip install jupyterlab
```



# *Editor Configurations*

## *Using Jupyter Lab*

Environment created above can be activated in any folder through `GIT Bash` using the following commands.

```shell
$ source /c/Python39/cv/Scripts/activate
$ jupyter lab
```

## *Using Visual Studio Code*

### Extensions to be installed

* Jupyter Extension for Visual Studio Code
* TabNine Autocomplete AI: JavaScript, Python, TypeScript, PHP, C/C++, HTML/CSS, Go, Java, Ruby, C#, Rust, SQL, Bash, Kotlin, Julia, Lua, OCaml, Perl, Haskell, React
