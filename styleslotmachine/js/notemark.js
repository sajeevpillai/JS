function notemarkLoad() {
    var val = UNIBERG_PAGE_ID;
    var url = 'sm://notemarkLoad/' + encodeURIComponent(JSON.stringify(val));
    var f = function() { window.location.href = url; };
    window.setTimeout(f, 100);
}

window.addEventListener('load', notemarkLoad, false);



var moved = false

function Box(inElement)
{
    var self = this;
    this.element = inElement;
    this.position = '0,0';
    this.element.addEventListener('touchstart', function(e) { return self.onTouchStart(e) }, false);
}

Box.prototype = {
    get position()
    {
        return this._position;
    },
    
    set position(pos)
    {
        this._position = pos;
        var components = pos.split(',');
        var x = components[0];
        var y = components[1];
        this.element.style.webkitTransform = 'translate(' + x + 'px, ' + y + 'px)';
    },
    
    get x()
    {
        return parseInt(this._position.split(',')[0]);
    },
    
    set x(inX)
    {
        var comps = this._position.split(',');
        comps[0] = inX;
        this._position = comps.join(',');
    },
    
    get y()
    {
        return parseInt(this._position.split(',')[1]);
    },
    
    set y(inY)
    {
        var comps = this._position.split(',');
        comps[1] = inY;
        this._position = comps.join(',');
    },
    
    onTouchStart: function(e)
    {
        moved = false
        if (e.targetTouches.length != 1)
        {
            return false;
        }
        
        this.startX = e.targetTouches[0].clientX;
        this.startY = e.targetTouches[0].clientY;
        
        var self = this;
        this.element.addEventListener('touchmove', function(e) { return self.onTouchMove(e) }, false);
        this.element.addEventListener('touchend', function(e) { return self.onTouchEnd(e) }, false);
        
        return false;
    },
    
    onTouchMove: function(e)
    {
        moved = true;
        e.preventDefault();
        if (e.targetTouches.length != 1)
        {
            return false;
        }
        var leftDelta = e.targetTouches[0].clientX - this.startX;
        var topDelta = e.targetTouches[0].clientY - this.startY;
        var newLeft = (this.x) + leftDelta;
        var newTop = (this.y) + topDelta;
        this.position = newLeft + ',' + newTop;
        this.startX = e.targetTouches[0].clientX;
        this.startY = e.targetTouches[0].clientY;
        return false;
    },
    
    onTouchEnd: function(e)
    {
        e.preventDefault();
        if (e.targetTouches.length > 0)
        {
            return false;
        }
        this.element.removeEventListener('touchmove', function(e) { return self.onTouchMove(e) }, false);
        this.element.removeEventListener('touchend', function(e) { return self.onTouchEnd(e) }, false);
        return false;
    },
}

function noteOpen(id, box)
{
    return function(event)
    {
        event.stopPropagation();
        if(!moved)
        {
            window.location.href = 'sm://noteOpen/%22' + id + '%22';
        }
        else
        {
            window.location.href = 'sm://setNoteCoordinates/%5B%22' + id + '%22%2C%5B' + box.x + '%2C' + box.y + '%5D%5D';
        }
    };
}

function addNote(id, x, y)
{
    var div = document.createElement('div');
    div.id = 'note-' + id;
    div.className = 'notemark';
    document.body.appendChild(div);
    box = new Box(div);
    box.position = x + ',' + y;
    div.addEventListener('touchend', noteOpen(id, box), false);
}

function deleteNote(id)
{
    var e = document.getElementById('note-' + id);
    e.parentNode.removeChild(e);
}
