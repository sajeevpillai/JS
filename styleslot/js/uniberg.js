document.write('<meta name="viewport" id="viewport" content="initial-scale = 1.0" />');

function call(f, v) {
    if(isTap()) {
        window.location.href = "sm://" + f + "/" + v;
    }
}

var minSwipeDistance = 30; // const
var tapToTurnArea = 50; // const

var isSingle = false;
var startX = -1000;
var startY = -1000;
var lastX = -1000;
var lastY = -1000;
var gestureDistance = -1000;

function abs(x) {
    if(x < 0) {
        return 0 - x;
    } else {
        return x;
    }
}

function sq(x) {
    return x * x;
}

function isTap() {
    return isSingle && startX == lastX && startY == lastY;
}

function distanceForTouches(touches) {
    var x0 = touches[0].screenX + window.pageXOffset;
    var y0 = touches[0].screenY + window.pageYOffset;
    var x1 = touches[1].screenX + window.pageXOffset;
    var y1 = touches[1].screenY + window.pageYOffset;
    
    return Math.sqrt(sq(x1-x0) + sq(y1-y0));
}


function jumpToParagraph(anchorName) {
    window.location.hash = anchorName;
}

function noteStart(event) {
    
}

function noteEnd(event, url) {
    if(isTap()) {
        event.stopPropagation();
        window.location.href = url;
    }
}

function readStart(event) {
    
}

function readEnd(event) {
    if(isTap()) {
        event.stopPropagation();
        window.location.href = 'sm://read';
    }
}

function instructionsStart(event) {
    
}

function instructionsEnd(event) {
    if(isTap()) {
        event.stopPropagation();
        window.location.href = 'sm://instructions';
    }
}

function linkStart(event) {

}

function linkEnd(event, url) {
    if(isTap()) {
        event.stopPropagation();
        window.location.href = url;
    }
}

function slideshowStart(event) {
}

function slideshowEnd(event, index, offset) {
    if(isTap()) {
        event.stopPropagation();
        window.location.href = 'sm://slideshow/' + index + '/' + offset;
    }
}

function tocStart(event) {
    
}

function tocEnd(event, page) {
    if(isTap()) {
        event.stopPropagation();
        window.location.href = 'sm://page/' + page;
    }
}

function paragraphStart(event, url) {
    window.location.href = url;
}

function paragraphEnd(event) {
    
}

function nextStart(event) {
    
}

function nextEnd(event) {
    if(isTap()) {
        event.stopPropagation();
        window.location.href = 'sm://page/+1';
    }
}

function documentStart(event) {
    var touches = event.touches;
    if(touches.length == 1) {
        isSingle = true;
        startX = touches[0].screenX + window.pageXOffset;
        startY = touches[0].screenY + window.pageYOffset;
        lastX = startX;
        lastY = startY;
    } else if(touches.length == 2) {
        event.preventDefault();
        gestureDistance = distanceForTouches(touches);
    }
}

document.addEventListener("touchstart", documentStart, false);

function documentMove(event) {
    var touches = event.touches;
    if(isSingle && touches.length == 1) {
        lastX = touches[0].screenX + window.pageXOffset;
        lastY = touches[0].screenY + window.pageYOffset;
    } else if(touches.length == 2) {
        isSingle = false;
        event.preventDefault();
        var newGestureDistance = distanceForTouches(touches);
        if(gestureDistance != 0 && newGestureDistance != gestureDistance) {
            window.location.href = 'sm://scale/' + (newGestureDistance / gestureDistance);
            gestureDistance = newGestureDistance;
        }
    } else {
        isSingle = false;
    }
}

document.addEventListener("touchmove", documentMove, false);

function documentEnd(event) {
    if(!isSingle || abs(startY - lastY) > minSwipeDistance) {
        return;
    }

    if(isTap()) {
        window.location.href = 'sm://nav/toggle';
        return;
    }
}

document.addEventListener("touchend", documentEnd, false);

function callIfTapped(event, f, v)
{
    if(isTap())
    {
        event.stopPropagation();
        var val = encodeURIComponent(JSON.stringify(v));
        window.location.href = "sm://" + f + "/" + val;
    }
}

function modalOpenWithURL(url) {
    v = '[%22 %22, %22' + encodeURIComponent(url) + '%22]';
    window.location.href = "sm://" + 'modalOpenWithURL' + "/" + v;
}

function itunesOpenWithURL(url) {
    v = '[%22 %22, %22' + encodeURIComponent(url) + '%22]';
    window.location.href = "sm://" + 'itunesOpenWithURL' + "/" + v;
}

function safariOpenURL(url) {
    v = '[%22 %22, %22' + encodeURIComponent(url) + '%22]';
    window.location.href = "sm://" + 'safariOpenURL' + "/" + v;
}
