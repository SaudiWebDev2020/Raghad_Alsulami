var world = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,1,2,1],
    [1,2,1,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,1,2,1],
    [1,2,1,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1],
]

var pacman = {
    top: 1,
    left: 1
}

var score = 0;

$(document).ready(function(){
    function updateWorld(){
        var worldBuilder = '';
        for(var y=0;y<world.length;y++){
            worldBuilder+='<div class="row">';
            for(var x=0;x<world[y].length;x++){
                if(world[y][x]==1){
                    worldBuilder+="<div class='wall'></div>";
                } else if(world[y][x]==2){
                    worldBuilder+="<div class='coin'></div>";
                } else if(world[y][x]==0){
                    worldBuilder+="<div class='blank'></div>";
                }
            }
            worldBuilder+='</div>';
        }
        // console.log(worldBuilder);
        $('#world').html(worldBuilder);
        $('#score').text(`${ score }`);
    }

    // updating pacman position
    function updatePacman(){
        $('#pacman').css('top', (pacman.top * 50)+'px');
        $('#pacman').css('left', (pacman.left * 50)+'px');
        console.log($('#pacman').css('left'))
    }

    $(document).keydown(function(event){
        if(event.keyCode==37){
            // move pacman left
            if(world[pacman.top][pacman.left-1] != 1){
                pacman.left --;
                $("#pacman").css('transform', 'rotate(180deg');
            }
        } else if(event.keyCode==38){
            // move pacman up
            if(world[pacman.top-1][pacman.left] != 1){
                pacman.top--;
                $("#pacman").css('transform', 'rotate(270deg');
            }
        } else if(event.keyCode==39){
            // move pacman right
            if(world[pacman.top][pacman.left+1] != 1){
                pacman.left ++;
                $("#pacman").css('transform', 'rotate(0deg');
            }
        } else if(event.keyCode==40){
            // move pacman down
            if(world[pacman.top+1][pacman.left] != 1){
                pacman.top++;
                $("#pacman").css('transform', 'rotate(90deg');
            }
        }
        console.log(world[pacman.top][pacman.left])
        if(world[pacman.top][pacman.left]==2){
            // pacman eats a coin
            world[pacman.top][pacman.left]=0;
            score += 50;
        }
        updateWorld();
        updatePacman();
    })
    updateWorld();
    updatePacman();
})