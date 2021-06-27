#!/bin/bash

WCDIR=/home/freq
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar

printf "\nPART 1: WORD COUNT MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                                        \
    -files      $WCDIR/step_one_map.py,$WCDIR/step_one_reduce.py                         \
    -mapper     $WCDIR/step_one_map.py                                       \
    -reducer    $WCDIR/step_one_reduce.py                                       \
    -input      Gutenberg/'*'                                       \
    -output     Word

printf "\nPART 2: TF-IDF MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                                        \
    -files      $WCDIR/step_two_map.py,$WCDIR/step_two_reduce.py                         \
    -mapper     $WCDIR/step_two_map.py                                      \
    -reducer    $WCDIR/step_two_reduce.py                                       \
    -input      Word/'*'                                       \
    -output     Out