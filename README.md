# µContest

Source code of my solutions to the [µContest](http://www.microcontest.com/) challenges.

## Prerequisites

Python 3.

## Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

Some solutions needs additional PyPI packages to be installed. See source code.

## Configuration

Copy the `.env.example` file to `.env` and fill in the configuration parameters which are self-explanatory.

## Usage

Example running the [base64 challenge](http://www.microcontest.com/contest.php?id=50):

    python -m crypto.base64

Replace the package and module names accordingly with the challenge category and name you want to run.