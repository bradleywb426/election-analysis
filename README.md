# An Analysis of Election Results

Analyzing of the results from a Colorado election as an audit of the election by request of a Colorado Board of Elections employee.

## Resources

- Data: election_results.csv
- Software:
  - Python 3.10.5
  - Visual Studio Code 1.68.0

## Overview

The Colorado Board of Elections has requested help in auditing the election results for a district in their state, and provided us with the election data for this district. The audit needed to provide the candidates, the total votes each received, and the winner. The Board of Elections then further asked to provide analysis on voter turnout by county.

## Results

Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

Based on the analysis of the election audit:

- A total of 369,711 votes were cast in this district for this congressional election.
  - This was determined by simply adding each new vote to a total vote variable
  - <img src=https://github.com/bradleywb426/election-analysis/blob/main/Resources/code_2.png width="300">

- The breakdown of votes by county was:
  - Jefferson county casted 38,855 votes, which was 10.5% of the total votes.
  - Denver county casted 306,055 votes, which was 82,8% of the total votes.
  - Arapahoe county casted 24,801 votes, which was 6.7% of the total votes.
   - The breakdown of votes by county was determined using a nested for loop that would go through every row of data and add a county to a list of counties if it was not already present, and then add any votes cast in said county to a county total
   - The percentage was then calculated by dividing the votes per county by the total votes for the election
   - <img src=https://github.com/bradleywb426/election-analysis/blob/main/Resources/code_1.png width="400">

- Denver county had the largest number of votes out of all counties, with 306,055 total votes.
  - The largest voter turnout was determined by checking the turnout with a given county against largest turnout variables, and updated the variable to match the checked county if the checked county has a larger turnout
  - <img src=https://github.com/bradleywb426/election-analysis/blob/main/Resources/code_3.png width="400">

- The breakdown of votes by candidates was:
  - Charles Casper Stockham won 85,213 votes, which was 23.0% of the total votes.
  - Diana DeGette won 272,892 votes, which was 73.8% of the total votes.
  - Raymon Anthony Doane won 11,606 votes, which was 3.1% of the total votes.
  - The breakdown of votes by candidates was determined using a nested for loop that went through every row of data and would add any unique candidate names to a list, and then add any votes cast for the candidate to their respective totals; while the percentages were calculated by dividing each candidates votes by the total votes
  - <img src=https://github.com/bradleywb426/election-analysis/blob/main/Resources/code_4.png width="450">

- The winner of the elections was Diana DeGette, who received 272,892 votes or 73.8% of the total votes.
  - The winner of the election was determined by checking a candidates vote count and percentage against the current winning count and percentage, and updating the winning stats if a candidate has a higher vote count and percentage
  - <img src=https://github.com/bradleywb426/election-analysis/blob/main/Resources/code_5.png width="600">

## Summary

In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. 

Give at least two examples of how this script can be modified to be used for other elections.
