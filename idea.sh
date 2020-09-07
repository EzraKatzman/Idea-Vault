#!/bin/bash

function idea() {
    cd
    printf "What's your idea? "
    read;
    # I never bothered setting path variables here, make sure to change them if you use this code
    python '/c/Users/Ezkat/desktop/projects/ideavault/posterboard.py' ${REPLY}
    printf "Would you like to make a Github repository for it? [Y/n]: "
    read answer
    case $answer in
        [yY]) 
            printf "Name the directory: "
            read dirname
            # And here too
            python '/c/Users/Ezkat/desktop/projects/ideavault/initializer.py' $dirname
            ;;
        *)
            printf "A repository was not created"
            exit 
            ;;
    esac
}
idea
