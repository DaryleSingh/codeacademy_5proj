let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

function generateTarget() {

return Math.floor(Math.random() * 9);

}


function compareGuesses(userguess,computerguess,secrettargetnumber) {

let computerguesscloseness=Math.abs(secrettargetnumber-computerguess);

let userguesscloseness=Math.abs(secrettargetnumber-userguess);

if (computerguesscloseness < userguesscloseness) {
    return false;
}
  
//if equal user will win
 if (userguesscloseness <= computerguesscloseness) {
   return true;
 }

}


function updateScore(winner) {

if(winner=="human") {
  humanScore=humanScore + 1
} else {
  computerScore=computerScore + 1
}

}


function advanceRound() {

currentRoundNumber =currentRoundNumber  + 1;

}


