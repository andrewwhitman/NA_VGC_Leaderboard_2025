# North America Video Game Masters Live Leaderboard

## Overview

The [NA VGC Masters Live Leaderboard](https://na-vgc-leaderboard-2025.ploomber.app/) aims to track the outcomes of the 2025 North America Pokémon VGC International Championships and update the [NA VG Masters division leaderboard](https://www.pokemon.com/us/play-pokemon/leaderboards/vg-masters/) in real time round by round. Qualification to the 2025 Pokémon World Championships is determined by a competitor's final placement in the seasonal leaderboard, which ends upon the conclusion of NAIC. While the official leaderboard won't be updated until at least a day after NAIC, creating much anticipation for its impact on Worlds qualification, [this one will provide projections and updates to the leaderboard every round](https://na-vgc-leaderboard-2025.ploomber.app/).

![Screenshot 2025-06-12 142857](https://github.com/user-attachments/assets/d435bca1-f2f5-44f7-b391-462274a42d28)


## How are Championship Points updated?

Championship Points (CP) are updated at the end of each round of NAIC. There are two parts to this update.

1. Determination of how much CP should be awarded given a competitor's current record and placement in the standings at NAIC.
2. Application of the awarded CP to the competitor's prior total given their major best finish limit outlook (bfl).

Using the [spreadsheet](https://docs.google.com/spreadsheets/d/1KlGSuI2w0KvsDAHs5fGnXiD6XsA7p0upouIN9PukFk0/edit?gid=831782724#gid=831782724) created and maintained by Austin Le, pre-NAIC CP totals and major bfl totals are used to achieve #2. The leaderboard covers the top 300 in NA, including all Automatic Qualifiers. Because of the bfl, only the 5 highest CP-earning major finishes are allowed to contribute to each competitor's final total. The following equation shows how the new total is calculated.

$$ CPpostNAIC = min(CPawardedNAIC - CPlowestMajorBFL, 0) + CPpreNAIC $$

The CP awarded at NAIC is meant to be cautiously predictive of the actual CP earned at NAIC. This means that it will fluctuate slightly, but it is not intended to vary drastically round by round. The further along in the tourney, the more accurate the CP awarded becomes. It is also not intended to be a representation of the minimum CP earned given a competitor's record and placement. The Qualification status is much more conservative and handles such scenarios. A round by round breakdown of how CP is awarded is below.

- Rounds 1-3
  - no CP awarded
- Round 4
  - top 512 if 4-0
- Round 5
  - top 256 if 5-0
  - top 512 if 4-0 into 4-1
- Round 6
  - standings are used and CP awarded is capped at top 256
  - top 128 if 6-0
- Round 7
  - standings CP capped at top 256
  - top 64 if 7-0
  - top 128 if 6-1
- Rounds 8-9
  - standings CP capped at top 128
  - top 32 if x-0
  - top 64 if x-1
- Round 10-11
  - standings CP capped at top 64
  - top 16 if x-0
  - top 32 if x-1
- Round 12
  - standings CP capped at top 32
  - top 16 if bye earned
- Each Top Cut Round
  - the appropriate CP is awarded upon a loss

Standings data is provided by [https://www.pokedata.ovh/standingsVGC/0000149/masters/](https://www.pokedata.ovh/standingsVGC/0000149/masters/). Thanks to Julien for help in providing data to test this app.


### CP Lock 🔒

When a competitor is no longer able to earn more CP at NAIC, their season total CP is locked on the leaderboard. This occurs if:
- not a participant
- disqualified
- dropped (including at the end of day 1 when not in day 2)
- incur 5 or more losses
- did not make top cut
- lose in top cut
- the end of the tournament

Each of these scenarios guarantee they cannot earn more CP than they've already been awarded, and only a poorly timed drop allows for their CP awarded to decrease.

## What do the Qualification emojis mean?

There are various emojis used to represent the qualification status of competitors as NAIC progresses.


### Automatic Qualifier 🎫

Automatic Qualifiers earn a direct invitation to the World Championships regardless of their standing in the leaderboard. AQs are awarded for winning a regional or special event, placing in the top 4 at an international, or placing in the top 4 at last year's Worlds. AQ invitations do not count toward the top 75 bar to determine NA's Worlds qualifiers. Prior to NAIC, NA has 14 AQs, 8 of which contribute to moving the top 75 bar down to the actual 83rd placement on the leaderboard. Once top 4 at NAIC is set, any additional AQs will be awarded.


### Travel Awards 🥇 🥈

Travel awards are earned by the top 12 and then next 4 competitors on the leaderboard at the conclusion of the 2025 season. Tier 1 TA (🥇) and Tier 2 TA (🥈) represent who currently holds these spots. These may change as the tournament progresses, and no effort is made to predict their final allocation.


### Qualification Status and the Top 75 Bar ✅ ❔ ❌

The qualification status of competitors who do not earn an AQ invitation depends on their final standing on the leaderboard. The top 75 non-AQ earn an invitation to Worlds. The following three emojis represent a competitor's qualification status:

✅ Certain or Very Likely Qualification

❔ Uncertain Qualification

❌ Very Unlikely or Impossible Qualification

Each competitor will receive one of these three statuses. ✅ and ❌ are intended to be roughly final. It would take a large swing of the bar for them to flip. The uncertain status (❔) is the default status of everyone on the leaderboard.

To determine the qualification status, two factors are considered:

1. the top 75 bar and its probable range
2. a player's best and worst case end of season CP total

The bar is determined as follows:
- Rounds 1-5
  - 960 CP estimate with a range of +-20 CP. This estimate comes from Yotam Cohen's [simulation work](https://colab.research.google.com/drive/1rM1C4sThO2PIDSFannmJzHhZDSC181ia?usp=sharing#scrollTo=HREB040-kOJ3).
- Rounds 6-11
  - Once standings data becomes incorporated into CP, the bar is recalculated, still with a range of +-20 CP.
- Rounds 12 through Top Cut
  - The bar is recalculated, but the range is refined. Its lowest is a dependent on how many AQ spots can effectively move the bar down. And its highest is a dependent on how many spots can still be earned that don't require an AQ invitation.


![image](https://github.com/user-attachments/assets/cd9e5bf6-cc5f-4629-9447-955319c4f857)

The top 75 bar and its range is illustrated by the blue highlighted row and red highlighted rows, respectively.

A player's best and worst case CP totals are determined by the best/worst they can do given their record. These won't be enumerated here.

Once these factors are calculated, then the qualification status is determined by:
- ✅ = A player's worst is higher than the high bar estimate
- ❌ = A player's best is lower than the low bar estimate
- ❔ Otherwise

If a player's CP is 🔒, then that value is used instead of best/worst cases.


## Contact

Feel free to reach me at [@Andrew_Whit_](https://x.com/Andrew_Whit_) on Twitter if you want to discuss anything here!
