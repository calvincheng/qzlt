<div id="top"></div>



<br />
<div align="center">
  <a href="https://github.com/calvincheng/qzlt">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">qzlt</h3>

  <p align="center">
    A Quizlet clone for the command line.
    <br />
    <a href="https://github.com/calvincheng/qzlt">View Demo</a>
    ·
    <a href="https://github.com/calvincheng/qzlt/issues">Report Bug</a>
    ·
    <a href="https://github.com/calvincheng/qzlt/issues">Request Feature</a>
  </p>
</div>



## About

<div align="center">
  <img src="docs/screenshot.gif" alt="Screenshot" width="640" />
</div>

Lorem ipsum

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Typer](https://typer.tiangolo.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



## Getting Started

### Prerequisites

#### python
```
brew install python@3.6
```

### Installation

#### GitHub
```
pip install qzlt
```

#### pip
```
pip install qzlt
```

Note that this will also create a hidden directory at `~/.qzlt`, where all study
sets will be held.

<p align="right">(<a href="#top">back to top</a>)</p>



## Usage

### Commands


### Creating and studying sets

Let's create a new set to start learning some common Chinese expressions. Run
```
> quiz sets create
Title: chinese
Description: Common expressions in Chinese
```
and follow the prompts to give your set a title and a description.

You can that the newly created set exists by listing all sets via
```
> quiz sets list
TITLE               DESCRIPTION
chinese             Common expressions in Chinese
```

By default, new sets are empty when created. Let's change that by adding some cards. Run
```
> quiz set add chinese
```

You'll be prompted to start giving your card a __term__ and a __definition__:
```
Term: 你好
Definition: Hello
Card added
```

Add as many cards as you want. When you're done, you can press `ctrl` and `C` to
exit.

To see all the cards you've just added, run
```
> quiz set list chinese
      TERM          DEFINITION
[0]   你好          Hello
[1]   再見          Goodbye
[2]   開心          Happy
[3]   傷心          Sad
[4]   蘋果          Apple
[5]   香蕉          Banana
```

You're all set! To study your new set, run
```
> quiz study chinese
```

To see all the study modes available, feel free to run
```
> quiz study --help
```

<p align="right">(<a href="#top">back to top</a>)</p>



## Roadmap

- [ ] Import from Anki
- [ ] Collect and display statistics (review heatmap, streaks, etc.)

See the [open issues](https://github.com/calvincheng/qzlt/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



## Contact

Calvin Cheng - calvin.cc.cheng@gmail.com

Project Link: [https://github.com/calvincheng/qzlt](https://github.com/calvincheng/qzlt)

<p align="right">(<a href="#top">back to top</a>)</p>
