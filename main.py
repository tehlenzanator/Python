'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

// Transcrypt'ed from Python, 2025-06-14 14:31:50
var __name__ = 'org.transcrypt.__runtime__';

function __nest__ (headObject, tailNames, value) {
    var current = headObject;
    if (tailNames != '') {
        var tailChain = tailNames.split ('.');
        var firstNewIndex = tailChain.length;
        for (var index = 0; index < tailChain.length; index++) {
            if (!current.hasOwnProperty (tailChain [index])) {
                firstNewIndex = index;
                break;
            }
            current = current [tailChain [index]];
        }
        for (var index = firstNewIndex; index < tailChain.length; index++) {
            current [tailChain [index]] = {};
            current = current [tailChain [index]];
        }
    }
    for (let attrib of Object.getOwnPropertyNames (value)) {
        Object.defineProperty (current, attrib, {
            get () {return value [attrib];},
            enumerable: true,
            configurable: true
        });
    }
}function __get__ (self, func, quotedFuncName) {
    if (self) {
        if (self.hasOwnProperty ('__class__') || typeof self == 'string' || self instanceof String) {
            if (quotedFuncName) {
                Object.defineProperty (self, quotedFuncName, {
                    value: function () {
                        var args = [] .slice.apply (arguments);
                        return func.apply (null, [self] .concat (args));
                    },
                    writable: true,
                    enumerable: true,
                    configurable: true
                });
            }
            return function () {
                var args = [] .slice.apply (arguments);
                return func.apply (null, [self] .concat (args));
            };
        }
        else {
            return func;
        }
    }
    else {
        return func;
    }
}var py_metatype = {
    __name__: 'type',
    __bases__: [],
    __new__: function (meta, name, bases, attribs) {
        var cls = function () {
            var args = [] .slice.apply (arguments);
            return cls.__new__ (args);
        };
        for (var index = bases.length - 1; index >= 0; index--) {
            var base = bases [index];
            for (var attrib in base) {
                var descrip = Object.getOwnPropertyDescriptor (base, attrib);
                if (descrip == null) {
                    continue;
                }
                Object.defineProperty (cls, attrib, descrip);
            }
            for (let symbol of Object.getOwnPropertySymbols (base)) {
                let descrip = Object.getOwnPropertyDescriptor (base, symbol);
                Object.defineProperty (cls, symbol, descrip);
            }
        }
        cls.__metaclass__ = meta;
        cls.__name__ = name.startsWith ('py_') ? name.slice (3) : name;
        cls.__bases__ = bases;
        for (var attrib in attribs) {
            var descrip = Object.getOwnPropertyDescriptor (attribs, attrib);
            Object.defineProperty (cls, attrib, descrip);
        }
        for (let symbol of Object.getOwnPropertySymbols (attribs)) {
            let descrip = Object.getOwnPropertyDescriptor (attribs, symbol);
            Object.defineProperty (cls, symbol, descrip);
        }
        return cls;
    }
};
py_metatype.__metaclass__ = py_metatype;
var object = {
    __init__: function (self) {},
    __metaclass__: py_metatype,
    __name__: 'object',
    __bases__: [],
    __new__: function (args) {
        var instance = Object.create (this, {__class__: {value: this, enumerable: true}});
        if ('__getattr__' in this || '__setattr__' in this) {
            instance = new Proxy (instance, {
                get: function (target, name) {
                    let result = target [name];
                    if (result == undefined) {
                        return target.__getattr__ (name);
                    }
                    else {
                        return result;
                    }
                },
                set: function (target, name, value) {
                    try {
                        target.__setattr__ (name, value);
                    }
                    catch (exception) {
                        target [name] = value;
                    }
                    return true;
                }
            });
        }
        this.__init__.apply (null, [instance] .concat (args));
        return instance;
    }
};
function __class__ (name, bases, attribs, meta) {
    if (meta === undefined) {
        meta = bases [0] .__metaclass__;
    }
    return meta.__new__ (meta, name, bases, attribs);
}function __kwargtrans__ (anObject) {
    anObject.__kwargtrans__ = null;
    anObject.constructor = Object;
    return anObject;
}
function __setproperty__ (anObject, name, descriptor) {
    if (!anObject.hasOwnProperty (name)) {
        Object.defineProperty (anObject, name, descriptor);
    }
}
function __specialattrib__ (attrib) {
    return (attrib.startswith ('__') && attrib.endswith ('__')) || attrib == 'constructor' || attrib.startswith ('py_');
}function len (anObject) {
    if (anObject === undefined || anObject === null) {
        return 0;
    }
    if (anObject.__len__ instanceof Function) {
        return anObject.__len__ ();
    }
    if (anObject.length !== undefined) {
        return anObject.length;
    }
    var length = 0;
    for (var attr in anObject) {
        if (!__specialattrib__ (attr)) {
            length++;
        }
    }
    return length;
}function __t__ (target) {
    return (
        target === undefined || target === null ? false :
        ['boolean', 'number'] .indexOf (typeof target) >= 0 ? target :
        target.__bool__ instanceof Function ? (target.__bool__ () ? target : false) :
        target.__len__ instanceof Function ?  (target.__len__ () !== 0 ? target : false) :
        target instanceof Function ? target :
        len (target) !== 0 ? target :
        false
    );
}
function int (any, radix) {
    if (any === false) {
        return 0;
    } else if (any === true) {
        return 1;
    } else {
        var number = parseInt(any, radix);
        if (isNaN (number)) {
            if (radix == undefined) {
                radix = 10;
            }
            throw ValueError('invalid literal for int() with base ' + radix + ': ' + any, new Error());
        }
        return number;
    }
}int.__name__ = 'int';
int.__bases__ = [object];
function bool (any) {
    return !!__t__ (any);
}bool.__name__ = 'bool';
bool.__bases__ = [int];
function repr (anObject) {
    if (anObject == null) {
        return 'None';
    }
    switch (typeof anObject) {
        case "undefined":
            return 'None';
        case "boolean":
            if (anObject) {
                return "True"
            } else {
                return "False";
            }
        case "number":
        case "string":
        case "symbol":
            return String (anObject);
        case "function":
            try {
                return String (anObject);
            } catch (e) {
                return "<function " + anObject.name + ">"
            }
    }
    if (anObject.__repr__) {
        return anObject.__repr__ ();
    } else if (anObject.__str__) {
        return anObject.__str__ ();
    } else {
        try {
            if (anObject.constructor == Object) {
                var result = '{';
                var comma = false;
                for (var attrib in anObject) {
                    if (!__specialattrib__ (attrib)) {
                        if (attrib.isnumeric ()) {
                            var attribRepr = attrib;
                        }
                        else {
                            var attribRepr = '\'' + attrib + '\'';
                        }
                        if (comma) {
                            result += ', ';
                        }
                        else {
                            comma = true;
                        }
                        result += attribRepr + ': ' + repr (anObject [attrib]);
                    }
                }
                result += '}';
                return result;
            }
            else {
                return String(anObject);
            }
        }
        catch (exception) {
            return '<object of type: ' + typeof anObject + '>';
        }
    }
}function min (nrOrSeq) {
    return arguments.length == 1 ? Math.min (...nrOrSeq) : Math.min (...arguments);
}var abs = Math.abs;
function __PyIterator__ (iterable) {
    this.iterable = iterable;
    this.index = 0;
}
__PyIterator__.prototype.__next__ = function() {
    if (this.index < this.iterable.length) {
        return this.iterable [this.index++];
    }
    else {
        throw StopIteration (new Error ());
    }
};
function range (start, stop, step) {
    if (stop == undefined) {
        stop = start;
        start = 0;
    }
    if (step == undefined) {
        step = 1;
    }
    if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
        return [];
    }
    var result = [];
    for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
        result.push(i);
    }
    return result;
}function list (iterable) {
    let instance = iterable ? Array.from (iterable) : [];
    return instance;
}

list.__name__ = 'list';
list.__bases__ = [object];
Object.defineProperty(Array.prototype, '__iter__', {value: function () {return new __PyIterator__ (this);}});
Object.defineProperty(Array.prototype, '__getslice__', {value: function (start, stop, step) {
    if (start < 0) {
        start = this.length + start;
    }
    if (stop == null) {
        stop = this.length;
    }
    else if (stop < 0) {
        stop = this.length + stop;
    }
    else if (stop > this.length) {
        stop = this.length;
    }
    if (step == 1) {
        return Array.prototype.slice.call(this, start, stop);
    }
    let result = list ([]);
    for (let index = start; index < stop; index += step) {
        result.push (this [index]);
    }
    return result;
}});
Object.defineProperty(Array.prototype, '__setslice__', {value: function (start, stop, step, source) {
    if (start < 0) {
        start = this.length + start;
    }
    if (stop == null) {
        stop = this.length;
    }
    else if (stop < 0) {
        stop = this.length + stop;
    }
    if (step == null) {
        Array.prototype.splice.apply (this, [start, stop - start] .concat (source));
    }
    else {
        let sourceIndex = 0;
        for (let targetIndex = start; targetIndex < stop; targetIndex += step) {
            this [targetIndex] = source [sourceIndex++];
        }
    }
}});
Object.defineProperty(Array.prototype, '__repr__', {value: function () {
    if (this.__class__ == set && !this.length) {
        return 'set()';
    }
    let result = !this.__class__ || this.__class__ == list ? '[' : this.__class__ == tuple ? '(' : '{';
    for (let index = 0; index < this.length; index++) {
        if (index) {
            result += ', ';
        }
        result += repr (this [index]);
    }
    if (this.__class__ == tuple && this.length == 1) {
        result += ',';
    }
    result += !this.__class__ || this.__class__ == list ? ']' : this.__class__ == tuple ? ')' : '}';    return result;
}});

Object.defineProperty(Array.prototype, 'append', {value: function (element) {
    this.push (element);
}});
Object.defineProperty(Array.prototype, 'py_clear', {value: function () {
    this.length = 0;
}});
Object.defineProperty(Array.prototype, 'extend', {value: function (aList) {
    this.push.apply (this, aList);
}});
Object.defineProperty(Array.prototype, 'insert', {value: function (index, element) {
    this.splice (index, 0, element);
}});
Object.defineProperty(Array.prototype, 'remove', {value: function (element) {
    let index = this.indexOf (element);
    if (index == -1) {
        throw ValueError ("list.remove(x): x not in list", new Error ());
    }
    this.splice (index, 1);
}});
Object.defineProperty(Array.prototype, 'index', {value: function (element) {
    return this.indexOf (element);
}});
Object.defineProperty(Array.prototype, 'py_pop', {value: function (index) {
    if (index == undefined) {
        return this.pop ();
    }
    else {
        return this.splice (index, 1) [0];
    }
}});
Object.defineProperty(Array.prototype, 'py_sort', {value: function () {
    __sort__.apply  (null, [this].concat ([] .slice.apply (arguments)));
}});
Object.defineProperty(Array.prototype, '__add__', {value: function (aList) {
    return list (this.concat (aList));
}});
Object.defineProperty(Array.prototype, '__mul__', {value: function (scalar) {
    let result = this;
    for (let i = 1; i < scalar; i++) {
        result = result.concat (this);
    }
    return result;
}});

function tuple (iterable) {
    let instance = iterable ? [] .slice.apply (iterable) : [];
    instance.__class__ = tuple;
    return instance;
}
tuple.__name__ = 'tuple';
tuple.__bases__ = [object];
function set (iterable) {
    let instance = [];
    if (iterable) {
        for (let index = 0; index < iterable.length; index++) {
            instance.add (iterable [index]);
        }
    }
    instance.__class__ = set;
    return instance;
}
set.__name__ = 'set';
set.__bases__ = [object];
Object.defineProperty(Array.prototype, '__bindexOf__', {value: function (element) {
    element += '';
    let mindex = 0;
    let maxdex = this.length - 1;
    while (mindex <= maxdex) {
        let index = (mindex + maxdex) / 2 | 0;
        let middle = this [index] + '';
        if (middle < element) {
            mindex = index + 1;
        }
        else if (middle > element) {
            maxdex = index - 1;
        }
        else {
            return index;
        }
    }
    return -1;
}});
Object.defineProperty(Array.prototype, 'add', {value: function (element) {
    if (this.indexOf (element) == -1) {
        this.push (element);
    }
}});
Object.defineProperty(Array.prototype, 'discard', {value: function (element) {
    var index = this.indexOf (element);
    if (index != -1) {
        this.splice (index, 1);
    }
}});
Object.defineProperty(Array.prototype, 'isdisjoint', {value: function (other) {
    this.sort ();
    for (let i = 0; i < other.length; i++) {
        if (this.__bindexOf__ (other [i]) != -1) {
            return false;
        }
    }
    return true;
}});
Object.defineProperty(Array.prototype, 'issuperset', {value: function (other) {
    this.sort ();
    for (let i = 0; i < other.length; i++) {
        if (this.__bindexOf__ (other [i]) == -1) {
            return false;
        }
    }
    return true;
}});
Object.defineProperty(Array.prototype, 'issubset', {value: function (other) {
    return set (other.slice ()) .issuperset (this);
}});
Object.defineProperty(Array.prototype, 'union', {value: function (other) {
    let result = set (this.slice () .sort ());
    for (let i = 0; i < other.length; i++) {
        if (result.__bindexOf__ (other [i]) == -1) {
            result.push (other [i]);
        }
    }
    return result;
}});
Object.defineProperty(Array.prototype, 'intersection', {value: function (other) {
    this.sort ();
    let result = set ();
    for (let i = 0; i < other.length; i++) {
        if (this.__bindexOf__ (other [i]) != -1) {
            result.push (other [i]);
        }
    }
    return result;
}});
Object.defineProperty(Array.prototype, 'difference', {value: function (other) {
    let sother = set (other.slice () .sort ());
    let result = set ();
    for (let i = 0; i < this.length; i++) {
        if (sother.__bindexOf__ (this [i]) == -1) {
            result.push (this [i]);
        }
    }
    return result;
}});
Object.defineProperty(Array.prototype, 'symmetric_difference', {value: function (other) {
    return this.union (other) .difference (this.intersection (other));
}});
Object.defineProperty(Array.prototype, 'py_update', {value: function () {
    let updated = [] .concat.apply (this.slice (), arguments) .sort ();
    this.py_clear ();
    for (let i = 0; i < updated.length; i++) {
        if (updated [i] != updated [i - 1]) {
            this.push (updated [i]);
        }
    }
}});
Object.defineProperty(Array.prototype, '__eq__', {value: function (other) {
    if (this.length != other.length) {
        return false;
    }
    if (this.__class__ == set) {
        this.sort ();
        other.sort ();
    }
    for (let i = 0; i < this.length; i++) {
        if (this [i] != other [i]) {
            return false;
        }
    }
    return true;
}});
Object.defineProperty(Array.prototype, '__ne__', {value: function (other) {
    return !this.__eq__ (other);
}});
Object.defineProperty(Array.prototype, '__le__', {value: function (other) {
    if (this.__class__ == set) {
        return this.issubset (other);
    }
    else {
        for (let i = 0; i < this.length; i++) {
            if (this [i] > other [i]) {
                return false;
            }
            else if (this [i] < other [i]) {
                return true;
            }
        }
        return true;
    }
}});
Object.defineProperty(Array.prototype, '__ge__', {value: function (other) {
    if (this.__class__ == set) {
        return this.issuperset (other);
    }
    else {
        for (let i = 0; i < this.length; i++) {
            if (this [i] < other [i]) {
                return false;
            }
            else if (this [i] > other [i]) {
                return true;
            }
        }
        return true;
    }
}});
Object.defineProperty(Array.prototype, '__lt__', {value: function (other) {
    return (
        this.__class__ == set ?
        this.issubset (other) && !this.issuperset (other) :
        !this.__ge__ (other)
    );
}});
Object.defineProperty(Array.prototype, '__gt__', {value: function (other) {
    return (
        this.__class__ == set ?
        this.issuperset (other) && !this.issubset (other) :
        !this.__le__ (other)
    );
}});
Object.defineProperty(Uint8Array.prototype, '__add__', {value: function (aBytes) {
    let result = new Uint8Array (this.length + aBytes.length);
    result.set (this);
    result.set (aBytes, this.length);
    return result;
}});
Object.defineProperty(Uint8Array.prototype, '__mul__', {value: function (scalar) {
    let result = new Uint8Array (scalar * this.length);
    for (let i = 0; i < scalar; i++) {
        result.set (this, i * this.length);
    }
    return result;
}});

function str (stringable) {
    if (stringable === null || typeof stringable === 'undefined') {
        return 'None';
    } else if (stringable.__str__) {
        return stringable.__str__ ();
    } else {
        return repr (stringable);
    }
}String.prototype.__class__ = str;
str.__name__ = 'str';
str.__bases__ = [object];
String.prototype.__iter__ = function () {new __PyIterator__ (this);};
String.prototype.__repr__ = function () {
    return (this.indexOf ('\'') == -1 ? '\'' + this + '\'' : '"' + this + '"') .py_replace ('\t', '\\t') .py_replace ('\n', '\\n');
};
String.prototype.__str__ = function () {
    return this;
};
String.prototype.capitalize = function () {
    return this.charAt (0).toUpperCase () + this.slice (1);
};
String.prototype.endswith = function (suffix) {
    if (suffix instanceof Array) {
        for (var i=0;i<suffix.length;i++) {
            if (this.slice (-suffix[i].length) == suffix[i])
                return true;
        }
    } else
        return suffix == '' || this.slice (-suffix.length) == suffix;
    return false;
};
String.prototype.find = function (sub, start) {
    return this.indexOf (sub, start);
};
String.prototype.__getslice__ = function (start, stop, step) {
    if (start < 0) {
        start = this.length + start;
    }
    if (stop == null) {
        stop = this.length;
    }
    else if (stop < 0) {
        stop = this.length + stop;
    }
    var result = '';
    if (step == 1) {
        result = this.substring (start, stop);
    }
    else {
        for (var index = start; index < stop; index += step) {
            result = result.concat (this.charAt(index));
        }
    }
    return result;
};
__setproperty__ (String.prototype, 'format', {
    get: function () {return __get__ (this, function (self) {
        var args = tuple ([] .slice.apply (arguments).slice (1));
        var autoIndex = 0;
        return self.replace (/\{(\w*)\}/g, function (match, key) {
            if (key == '') {
                key = autoIndex++;
            }
            if (key == +key) {
                return args [key] === undefined ? match : str (args [key]);
            }
            else {
                for (var index = 0; index < args.length; index++) {
                    if (typeof args [index] == 'object' && args [index][key] !== undefined) {
                        return str (args [index][key]);
                    }
                }
                return match;
            }
        });
    });},
    enumerable: true
});
String.prototype.isalnum = function () {
    return /^[0-9a-zA-Z]{1,}$/.test(this)
};
String.prototype.isalpha = function () {
    return /^[a-zA-Z]{1,}$/.test(this)
};
String.prototype.isdecimal = function () {
    return /^[0-9]{1,}$/.test(this)
};
String.prototype.isdigit = function () {
    return this.isdecimal()
};
String.prototype.islower = function () {
    return /^[a-z]{1,}$/.test(this)
};
String.prototype.isupper = function () {
    return /^[A-Z]{1,}$/.test(this)
};
String.prototype.isspace = function () {
    return /^[\s]{1,}$/.test(this)
};
String.prototype.isnumeric = function () {
    return !isNaN (parseFloat (this)) && isFinite (this);
};
String.prototype.join = function (strings) {
    strings = Array.from (strings);
    return strings.join (this);
};
String.prototype.lower = function () {
    return this.toLowerCase ();
};
String.prototype.py_replace = function (old, aNew, maxreplace) {
    return this.split (old, maxreplace) .join (aNew);
};
String.prototype.lstrip = function () {
    return this.replace (/^\s*/g, '');
};
String.prototype.rfind = function (sub, start) {
    return this.lastIndexOf (sub, start);
};
String.prototype.rsplit = function (sep, maxsplit) {
    if (sep == undefined || sep == null) {
        sep = /\s+/;
        var stripped = this.strip ();
    }
    else {
        var stripped = this;
    }
    if (maxsplit == undefined || maxsplit == -1) {
        return stripped.split (sep);
    }
    else {
        var result = stripped.split (sep);
        if (maxsplit < result.length) {
            var maxrsplit = result.length - maxsplit;
            return [result.slice (0, maxrsplit) .join (sep)] .concat (result.slice (maxrsplit));
        }
        else {
            return result;
        }
    }
};
String.prototype.rstrip = function () {
    return this.replace (/\s*$/g, '');
};
String.prototype.py_split = function (sep, maxsplit) {
    if (sep == undefined || sep == null) {
        sep = /\s+/;
        var stripped = this.strip ();
    }
    else {
        var stripped = this;
    }
    if (maxsplit == undefined || maxsplit == -1) {
        return stripped.split (sep);
    }
    else {
        var result = stripped.split (sep);
        if (maxsplit < result.length) {
            return result.slice (0, maxsplit).concat ([result.slice (maxsplit).join (sep)]);
        }
        else {
            return result;
        }
    }
};
String.prototype.startswith = function (prefix) {
    if (prefix instanceof Array) {
        for (var i=0;i<prefix.length;i++) {
            if (this.indexOf (prefix [i]) == 0)
                return true;
        }
    } else
        return this.indexOf (prefix) == 0;
    return false;
};
String.prototype.strip = function () {
    return this.trim ();
};
String.prototype.upper = function () {
    return this.toUpperCase ();
};
String.prototype.__mul__ = function (scalar) {
    var result = '';
    for (var i = 0; i < scalar; i++) {
        result = result + this;
    }
    return result;
};
String.prototype.__rmul__ = String.prototype.__mul__;
function __setdoc__ (docString) {
    this.__doc__ = docString;
    return this;
}
__setproperty__ (Function.prototype, '__setdoc__', {value: __setdoc__, enumerable: false});
function __mod__ (a, b) {
    if (typeof a == 'object' && '__mod__' in a) {
        return a.__mod__ (b);
    }
    else if (typeof b == 'object' && '__rmod__' in b) {
        return b.__rmod__ (a);
    }
    else {
        return ((a % b) + b) % b;
    }
}var BaseException =  __class__ ('BaseException', [object], {
	__module__: __name__,
});
var Exception =  __class__ ('Exception', [BaseException], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		var kwargs = {};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						default: kwargs [__attrib0__] = __allkwargs0__ [__attrib0__];
					}
				}
				delete kwargs.__kwargtrans__;
			}
			var args = [].slice.apply (arguments).slice (1, __ilastarg0__ + 1);
		}
		else {
			var args = [];
		}
		self.__args__ = args;
		if (kwargs.error != null) {
			self.stack = kwargs.error.stack;
		}
		else if (Error) {
			self.stack = new Error ().stack;
		}
		else {
			self.stack = 'No stack trace available';
		}
	});},
	get __repr__ () {return __get__ (this, function (self) {
		if (len (self.__args__) > 1) {
			return '{}{}'.format (self.__class__.__name__, repr (tuple (self.__args__)));
		}
		else if (len (self.__args__)) {
			return '{}({})'.format (self.__class__.__name__, repr (self.__args__[0]));
		}
		else {
			return '{}()'.format (self.__class__.__name__);
		}
	});},
	get __str__ () {return __get__ (this, function (self) {
		if (len (self.__args__) > 1) {
			return str (tuple (self.__args__));
		}
		else if (len (self.__args__)) {
			return str (self.__args__[0]);
		}
		else {
			return '';
		}
	});}
});
__class__ ('IterableError', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, error) {
		Exception.__init__ (self, "Can't iterate over non-iterable", __kwargtrans__ ({error: error}));
	});}
});
var StopIteration =  __class__ ('StopIteration', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, error) {
		Exception.__init__ (self, 'Iterator exhausted', __kwargtrans__ ({error: error}));
	});}
});
var ValueError =  __class__ ('ValueError', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, message, error) {
		Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
	});}
});
__class__ ('KeyError', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, message, error) {
		Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
	});}
});
__class__ ('AssertionError', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, message, error) {
		if (message) {
			Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
		}
		else {
			Exception.__init__ (self, __kwargtrans__ ({error: error}));
		}
	});}
});
__class__ ('NotImplementedError', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, message, error) {
		Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
	});}
});
__class__ ('IndexError', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, message, error) {
		Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
	});}
});
__class__ ('AttributeError', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, message, error) {
		Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
	});}
});
__class__ ('py_TypeError', [Exception], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, message, error) {
		Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
	});}
});
var Warning =  __class__ ('Warning', [Exception], {
	__module__: __name__,
});
__class__ ('UserWarning', [Warning], {
	__module__: __name__,
});
__class__ ('DeprecationWarning', [Warning], {
	__module__: __name__,
});
__class__ ('RuntimeWarning', [Warning], {
	__module__: __name__,
});
var __sort__ = function (iterable, key, reverse) {
	if (typeof key == 'undefined' || (key != null && key.hasOwnProperty ("__kwargtrans__"))) {		var key = null;
	}	if (typeof reverse == 'undefined' || (reverse != null && reverse.hasOwnProperty ("__kwargtrans__"))) {		var reverse = false;
	}	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'iterable': var iterable = __allkwargs0__ [__attrib0__]; break;
					case 'key': var key = __allkwargs0__ [__attrib0__]; break;
					case 'reverse': var reverse = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	if (key) {
		iterable.sort ((function __lambda__ (a, b) {
			if (arguments.length) {
				var __ilastarg0__ = arguments.length - 1;
				if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
					var __allkwargs0__ = arguments [__ilastarg0__--];
					for (var __attrib0__ in __allkwargs0__) {
						switch (__attrib0__) {
							case 'a': var a = __allkwargs0__ [__attrib0__]; break;
							case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						}
					}
				}
			}
			return (key (a) > key (b) ? 1 : -(1));
		}));
	}
	else {
		iterable.sort ();
	}
	if (reverse) {
		iterable.reverse ();
	}
};
var filter = function (func, iterable) {
	if (func == null) {
		var func = bool;
	}
	return (function () {
		var __accu0__ = [];
		for (var item of iterable) {
			if (func (item)) {
				__accu0__.append (item);
			}
		}
		return __accu0__;
	}) ();
};
var divmod = function (n, d) {
	return [Math.floor (n / d), __mod__ (n, d)];
};
var __Terminal__ =  __class__ ('__Terminal__', [object], {
	__module__: __name__,
	get print () {return __get__ (this, function (self) {
		var sep = ' ';
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'sep': var sep = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
			var args = [].slice.apply (arguments).slice (1, __ilastarg0__ + 1);
		}
		else {
			var args = [];
		}
		var length = len (args);
		if (length < 1) {
			console.log ();
		}
		else if (length == 1) {
			console.log (args[0]);
		}
		else {
			console.log (sep.join ((function () {
				var __accu0__ = [];
				for (var arg of args) {
					__accu0__.append (str (arg));
				}
				return __accu0__;
			}) ()));
		}
	});}
});
var __terminal__ = __Terminal__ ();
var print = __terminal__.print;
__terminal__.input;

// Transcrypt'ed from Python, 2025-06-14 14:31:50
var pi = Math.PI;
var e = Math.E;
var exp = Math.exp;
var expm1 = function (x) {
	return Math.exp (x) - 1;
};
var log = function (x, base) {
	return (base === undefined ? Math.log (x) : Math.log (x) / Math.log (base));
};
var log1p = function (x) {
	return Math.log (x + 1);
};
var log2 = function (x) {
	return Math.log (x) / Math.LN2;
};
var log10 = function (x) {
	return Math.log (x) / Math.LN10;
};
var pow = Math.pow;
var sqrt = Math.sqrt;
var sin = Math.sin;
var cos = Math.cos;
var tan = Math.tan;
var asin = Math.asin;
var acos = Math.acos;
var atan = Math.atan;
var atan2 = Math.atan2;
var hypot = Math.hypot;
var degrees = function (x) {
	return (x * 180) / Math.PI;
};
var radians = function (x) {
	return (x * Math.PI) / 180;
};
var sinh = Math.sinh;
var cosh = Math.cosh;
var tanh = Math.tanh;
var asinh = Math.asinh;
var acosh = Math.acosh;
var atanh = Math.atanh;
var floor = Math.floor;
var ceil = Math.ceil;
var trunc = Math.trunc;
var isnan = isNaN;
var inf = Infinity;
var nan = NaN;
var modf = function (n) {
	var sign = (n >= 0 ? 1 : -(1));
	var __left0__ = divmod (abs (n), 1);
	var f = __left0__ [0];
	var mod = __left0__ [1];
	return [mod * sign, f * sign];
};

var __module_math__ = /*#__PURE__*/Object.freeze({
    __proto__: null,
    pi: pi,
    e: e,
    exp: exp,
    expm1: expm1,
    log: log,
    log1p: log1p,
    log2: log2,
    log10: log10,
    pow: pow,
    sqrt: sqrt,
    sin: sin,
    cos: cos,
    tan: tan,
    asin: asin,
    acos: acos,
    atan: atan,
    atan2: atan2,
    hypot: hypot,
    degrees: degrees,
    radians: radians,
    sinh: sinh,
    cosh: cosh,
    tanh: tanh,
    asinh: asinh,
    acosh: acosh,
    atanh: atanh,
    floor: floor,
    ceil: ceil,
    trunc: trunc,
    isnan: isnan,
    inf: inf,
    nan: nan,
    modf: modf
});

// Transcrypt'ed from Python, 2025-06-14 14:31:50
var math$2 = {};
__nest__ (math$2, '', __module_math__);
var _array = (function () {
	var __accu0__ = [];
	for (var i = 0; i < 624; i++) {
		__accu0__.append (0);
	}
	return __accu0__;
}) ();
var _index = 0;
var _bitmask1 = Math.pow (2, 32) - 1;
var _bitmask2 = Math.pow (2, 31);
var _bitmask3 = Math.pow (2, 31) - 1;
var _fill_array = function () {
	for (var i = 0; i < 624; i++) {
		var y = (_array[i] & _bitmask2) + (_array[__mod__ (i + 1, 624)] & _bitmask3);
		if (__mod__ (y, 2) != 0) ;
	}
};
var _random_integer = function () {
	if (_index == 0) {
		_fill_array ();
	}
	var y = _array[_index];
	y ^= y >> 11;
	y ^= y << 7 & 2636928640;
	y ^= y << 15 & 4022730752;
	y ^= y >> 18;
	_index = __mod__ (_index + 1, 624);
	return y;
};
var seed = function (x) {
	if (typeof x == 'undefined' || (x != null && x.hasOwnProperty ("__kwargtrans__"))) {		var x = int (_bitmask3 * Math.random ());
	}};
var randint = function (a, b) {
	return a + __mod__ (_random_integer (), (b - a) + 1);
};
var choice = function (seq) {
	return seq[randint (0, len (seq) - 1)];
};
var random$2 = function () {
	return _random_integer () / _bitmask3;
};
var shuffle = function (x) {
	for (var i of range (len (x) - 1, 0, -(1))) {
		math$2.floor (random$2 () * (i + 1));
		x[i];
	}
};
seed ();

var __module_random__ = /*#__PURE__*/Object.freeze({
    __proto__: null,
    _array: _array,
    get _index () { return _index; },
    _bitmask1: _bitmask1,
    _bitmask2: _bitmask2,
    _bitmask3: _bitmask3,
    _fill_array: _fill_array,
    _random_integer: _random_integer,
    seed: seed,
    randint: randint,
    choice: choice,
    random: random$2,
    shuffle: shuffle
});

// Transcrypt'ed from Python, 2025-06-14 14:31:50
var math$1 = {};
var random$1 = {};
__nest__ (random$1, '', __module_random__);
__nest__ (math$1, '', __module_math__);
var init_cache = function () {
	Cache.role_map = {['miner']: miner_action, ['hauler']: hauler_action, ['worker']: worker_action};
};
var do_action = function (creep) {
	try {
		var role_function = Cache.role_map[creep.memory.role];
		role_function (creep);
	}
	catch (__except0__) {
		print (((('No role function for creep ' + creep.name) + ' with role ') + creep.memory.role) + '!');
	}
};
var hauler_action = function (creep) {
	if (creep.memory.target_room == null) {
		print (('Hauler ' + creep.name) + ' is lacking target_room.');
		return ;
	}
	if (creep.room.name != creep.memory.target_room) {
		var exitpos = creep.pos.findClosestByPath (Game.map.findRoute (creep.room.name, creep.memory.target_room)[0].exit, {['ignoreCreeps']: true});
		creep.moveTo (exitpos);
		return ;
	}
	if (creep.memory.task == null || (creep.memory.task == 'sucking' || creep.memory.task == 'picking') && creep.store.getFreeCapacity () == 0 || creep.memory.task == 'filling' && creep.store[RESOURCE_ENERGY] == 0) {
		creep.memory.task = 'idle';
	}
	var target = null;
	if (creep.memory.task != 'idle') {
		var target = Game.getObjectById (creep.memory.target);
		if (target == null || creep.memory.task == 'filling' && target.store.getFreeCapacity (RESOURCE_ENERGY) == 0 || creep.memory.task == 'sucking' && target.store[RESOURCE_ENERGY] < 20) {
			creep.memory.task = 'idle';
		}
	}
	if (creep.memory.task == 'idle' && creep.store[RESOURCE_ENERGY] > 0) {
		var fill_structs = filter ((function __lambda__ (s) {
			return [STRUCTURE_EXTENSION, STRUCTURE_SPAWN].includes (s.structureType) && s.store.getFreeCapacity (RESOURCE_ENERGY) > 0;
		}), creep.room.find (FIND_MY_STRUCTURES));
		if (len (fill_structs) > 0) {
			var target = creep.pos.findClosestByPath (fill_structs, {['ignoreCreeps']: true});
			if (target != null) {
				creep.memory.target = target.id;
				creep.memory.task = 'filling';
			}
			else {
				print ('No path to fill structures for hauler ' + creep.name);
			}
		}
		else {
			var fill_creeps = filter ((function __lambda__ (c) {
				return c.memory.role == 'worker' && c.store.getFreeCapacity (RESOURCE_ENERGY) > c.store.getUsedCapacity (RESOURCE_ENERGY);
			}), creep.room.find (FIND_MY_CREEPS));
			if (len (fill_creeps) > 0) {
				var target = creep.pos.findClosestByPath (fill_creeps, {['ignoreCreeps']: true});
				if (target != null) {
					creep.memory.target = target.id;
					creep.memory.task = 'filling';
				}
				else {
					print ('No path to fill creeps for hauler ' + creep.name);
				}
			}
		}
	}
	if (creep.memory.task == 'idle' && creep.store.getFreeCapacity () > 0) {
		var grab_piles = filter ((function __lambda__ (r) {
			return r.resourceType == RESOURCE_ENERGY && r.amount > 100;
		}), creep.room.find (FIND_DROPPED_RESOURCES));
		if (len (grab_piles) > 0) {
			var target = creep.pos.findClosestByPath (grab_piles, {['ignoreCreeps']: true});
			if (target != null) {
				creep.memory.target = target.id;
				creep.memory.task = 'picking';
			}
			else {
				print ('No path to grab piles for hauler ' + creep.name);
			}
		}
		else {
			var grab_containers = filter ((function __lambda__ (s) {
				return s.structureType == STRUCTURE_CONTAINER && s.store[RESOURCE_ENERGY] > 100;
			}), creep.room.find (FIND_STRUCTURES));
			if (len (grab_containers) > 0) {
				var target = creep.pos.findClosestByPath (grab_containers, {['ignoreCreeps']: true});
				if (target != null) {
					creep.memory.target = target.id;
					creep.memory.task = 'sucking';
				}
				else {
					print ('No path to grab containers for hauler ' + creep.name);
				}
			}
		}
	}
	if (creep.memory.task == 'picking' && target != null) {
		if (creep.pos.isNearTo (target)) {
			creep.pickup (target);
			creep.memory.task = 'idle';
		}
		else {
			creep.moveTo (target);
		}
	}
	if (creep.memory.task == 'sucking' && target != null) {
		if (creep.pos.isNearTo (target)) {
			creep.withdraw (target, RESOURCE_ENERGY);
			creep.memory.task = 'idle';
		}
		else {
			creep.moveTo (target);
		}
	}
	if (creep.memory.task == 'filling' && target != null) {
		if (creep.pos.isNearTo (target)) {
			creep.transfer (target, RESOURCE_ENERGY);
			creep.memory.task = 'idle';
		}
		else {
			creep.moveTo (target);
		}
	}
	if (creep.memory.task == 'idle' && ([0, 1, 48, 49].includes (creep.pos.x) || [0, 1, 48, 49].includes (creep.pos.y))) {
		creep.moveTo (creep.room.controller);
	}
};
var miner_action = function (creep) {
	if (creep.memory.target_room == null) {
		print (('Miner ' + creep.name) + ' is lacking target_room.');
		return ;
	}
	if (creep.room.name != creep.memory.target_room) {
		var exitpos = creep.pos.findClosestByPath (Game.map.findRoute (creep.room.name, creep.memory.target_room)[0].exit, {['ignoreCreeps']: true});
		creep.moveTo (exitpos);
		return ;
	}
	var target = Game.getObjectById (creep.memory.target);
	if (target == null) {
		print (('Miner ' + creep.name) + ' is lacking target source.');
		return ;
	}
	if (creep.memory.container == null) {
		creep.memory.container = '';
		var containers = filter ((function __lambda__ (s) {
			return s.structureType == STRUCTURE_CONTAINER;
		}), target.pos.findInRange (FIND_STRUCTURES, 1));
		if (containers != '') {
			creep.memory.container = _.sample (containers).id;
		}
	}
	var container = null;
	if (creep.memory.container != null && creep.memory.container != '') {
		var container = Game.getObjectById (creep.memory.container);
	}
	if (container) {
		if (creep.pos.isEqualTo (container)) {
			creep.harvest (target);
		}
		else {
			creep.moveTo (container);
		}
	}
	else if (creep.pos.isNearTo (target)) {
		creep.harvest (target);
	}
	else {
		creep.moveTo (target);
	}
};
var worker_action = function (creep) {
	if (creep.memory.target_room == null) {
		print (('Worker ' + creep.name) + ' is lacking target_room.');
		return ;
	}
	if (creep.room.name != creep.memory.target_room) {
		var exitpos = creep.pos.findClosestByPath (Game.map.findRoute (creep.room.name, creep.memory.target_room)[0].exit, {['ignoreCreeps']: true});
		creep.moveTo (exitpos);
		return ;
	}
	if (creep.memory.task != 'idle') {
		if (creep.memory.check_delay == null) {
			creep.memory.check_delay = 0;
		}
		else {
			creep.memory.check_delay += 1;
			if (creep.memory.check_delay > 100 && creep.store[RESOURCE_ENERGY] == 0) {
				creep.memory.task = 'idle';
			}
		}
	}
	var target = null;
	if (creep.memory.task != 'idle') {
		var target = Game.getObjectById (creep.memory.target);
		if (target == null || creep.memory.task == 'repairing' && target.hits >= target.hitsMax) {
			creep.memory.task = 'idle';
		}
	}
	if (creep.memory.task == 'idle') {
		if (creep.room.controller.ticksToDowngrade < CONTROLLER_DOWNGRADE[creep.room.controller.level] - 3000) {
			creep.memory.target = creep.room.controller.id;
			creep.memory.task = 'upgrading';
			var target = creep.room.controller;
			creep.memory.check_delay = 0;
		}
		else {
			var repair_structs = filter ((function __lambda__ (s) {
				return s.my && s.hits < s.hitsMax || [STRUCTURE_ROAD, STRUCTURE_CONTAINER].includes (s.structureType) && s.hits * 2 < s.hitsMax;
			}), creep.room.find (FIND_STRUCTURES));
			if (len (repair_structs) > 0) {
				var target = creep.pos.findClosestByPath (repair_structs, {['ignoreCreeps']: true, ['range']: 3});
				if (target != null) {
					creep.memory.target = target.id;
					creep.memory.task = 'repairing';
					creep.memory.check_delay = 0;
				}
				else {
					print ('No path to repair structures for worker ' + creep.name);
				}
			}
			else {
				var sites = creep.room.find (FIND_MY_CONSTRUCTION_SITES);
				if (len (sites) > 0) {
					var target = creep.pos.findClosestByPath (sites, {['ignoreCreeps']: true, ['range']: 3});
					if (target != null) {
						creep.memory.target = target.id;
						creep.memory.task = 'building';
						creep.memory.check_delay = 0;
					}
					else {
						print ('No path to construction sites for worker ' + creep.name);
					}
				}
				else {
					creep.memory.target = creep.room.controller.id;
					creep.memory.task = 'upgrading';
					var target = creep.room.controller;
					creep.memory.check_delay = 0;
				}
			}
		}
	}
	if (creep.memory.task == 'upgrading' && target != null) {
		if (creep.pos.inRangeTo (target, 3)) {
			creep.upgradeController (target);
		}
		else {
			creep.moveTo (target);
		}
	}
	if (creep.memory.task == 'repairing' && target != null) {
		if (creep.pos.inRangeTo (target, 3)) {
			creep.repair (target);
		}
		else {
			creep.moveTo (target);
		}
	}
	if (creep.memory.task == 'building' && target != null) {
		if (creep.pos.inRangeTo (target, 3)) {
			creep.build (target);
		}
		else {
			creep.moveTo (target);
		}
	}
};

var __module_creep_roles__ = /*#__PURE__*/Object.freeze({
    __proto__: null,
    init_cache: init_cache,
    do_action: do_action,
    hauler_action: hauler_action,
    miner_action: miner_action,
    worker_action: worker_action
});

// Transcrypt'ed from Python, 2025-06-14 14:31:50
var creep_roles = {};
var math = {};
var random = {};
__nest__ (random, '', __module_random__);
__nest__ (math, '', __module_math__);
__nest__ (creep_roles, '', __module_creep_roles__);
exports.my_memory = Memory;
exports.my_memory = RawMemory._parsed;
if (exports.my_memory.reset_log == null) {
	exports.my_memory.reset_log = [];
}
if (exports.my_memory.last_reset != null) {
	print ((((' ======= Global reset! Time of reset: ' + Game.time) + ' Time since last reset: ') + (Game.time - exports.my_memory.last_reset)) + ' ======= ');
	exports.my_memory.reset_log.append (Game.time - exports.my_memory.last_reset);
	while (len (exports.my_memory.reset_log) > 10) {
		exports.my_memory.reset_log.py_pop (0);
	}
}
exports.my_memory.last_reset = Game.time;
var Cache = {};
creep_roles.init_cache ();
Cache.rooms = {};
if (exports.my_memory.creeps == null) {
	exports.my_memory.creeps = {};
}
if (exports.my_memory.rooms == null) {
	exports.my_memory.rooms = {};
}
if (exports.my_memory.spawns == null) {
	exports.my_memory.spawns = {};
}
var body_shorthand = function (body) {
	var body_count = {};
	for (var part of body) {
		if (body_count[part] == null) {
			body_count[part] = 1;
		}
		else {
			body_count[part] += 1;
		}
	}
	var outstring = '';
	for (var part_type of Object.keys (body_count)) {
		outstring += (('' + body_count[part_type]) + part_type) + ' ';
	}
	return outstring;
};
var main = function () {
	delete global.Memory;
	global.Memory = exports.my_memory;
	RawMemory._parsed = exports.my_memory;
	Cache.owned_rooms = [];
	for (var room_name of Object.keys (Game.rooms)) {
		var room = Game.rooms[room_name];
		if (room.controller != null && room.controller.my) {
			if (Cache.rooms[room_name] == null) {
				Cache.rooms[room_name] = {};
			}
			Cache.owned_rooms.append (room_name);
			Cache.rooms[room_name].current_work_parts = 0;
			Cache.rooms[room_name].current_carry_parts = 0;
		}
	}
	for (var name of Object.keys (Memory.creeps)) {
		if (Game.creeps[name] == null) {
			print ('RIP ' + name);
			delete Memory.creeps[name];
		}
	}
	for (var name of Object.keys (Memory.rooms)) {
		if (Game.rooms[name] == null) {
			delete Memory.rooms[name];
		}
	}
	for (var name of Object.keys (Memory.spawns)) {
		if (Game.spawns[name] == null) {
			delete Memory.spawns[name];
		}
	}
	for (var name of Object.keys (Game.creeps)) {
		var creep = Game.creeps[name];
		if (!(creep.spawning)) {
			creep_roles.do_action (creep);
		}
	}
	for (var spawn_name of Object.keys (Game.spawns)) {
		var spawn = Game.spawns[spawn_name];
		if (spawn.hits < spawn.hitsMax && spawn.room.controller.my) {
			spawn.room.controller.activateSafeMode ();
		}
	}
	if (__mod__ (Game.time, 3) == 0) {
		var timestamp = Game.time.toString ().py_split ('');
		var timecode = 'snek ';
		for (var i = 0; i < 4; i++) {
			var char = timestamp[(i + len (timestamp)) - 4];
			if (char == '0') {
				timecode += '--';
			}
			if (char == '1') {
				timecode += '-~';
			}
			if (char == '2') {
				timecode += '~-';
			}
			if (char == '3') {
				timecode += '~~';
			}
			if (char == '4') {
				timecode += '=-';
			}
			if (char == '5') {
				timecode += '-=';
			}
			if (char == '6') {
				timecode += '==';
			}
			if (char == '7') {
				timecode += '=~';
			}
			if (char == '8') {
				timecode += '~=';
			}
			if (char == '9') {
				timecode += '<>';
			}
		}
		timecode += ':3';
		for (var name of Object.keys (Game.creeps)) {
			var creep = Game.creeps[name];
			if (creep.memory.role == 'worker' && Cache.rooms[creep.memory.target_room] != null) {
				Cache.rooms[creep.memory.target_room].current_work_parts += creep.getActiveBodyparts (WORK);
			}
			if (creep.memory.role == 'hauler' && (creep.ticksToLive > 150 || creep.spawning) && Cache.rooms[creep.memory.target_room] != null) {
				Cache.rooms[creep.memory.target_room].current_carry_parts += creep.getActiveBodyparts (CARRY);
			}
		}
		var num_spawns = 0;
		for (var room_name of Cache.owned_rooms) {
			var room = Game.rooms[room_name];
			var spawns = room.find (FIND_MY_SPAWNS);
			var used_energy = 0;
			for (var spawn of spawns) {
				if (!(spawn.isActive ())) {
					continue;
				}
				if (spawn.spawning) {
					if (spawn.spawning.remainingTime <= 1) {
						var creeps = spawn.pos.findInRange (FIND_MY_CREEPS, 1);
						for (var creep of creeps) {
							creep.moveTo (room.controller);
						}
					}
					continue;
				}
				var name = '';
				for (var i = 0; i < num_spawns; i++) {
					name += 's';
				}
				name += timecode;
				var creep_names = filter ((function __lambda__ (n) {
					return Game.creeps[n].memory.target_room == room.name;
				}), Object.keys (Game.creeps));
				var current_creeps = [];
				for (var creep_name of creep_names) {
					current_creeps.append (Game.creeps[creep_name]);
				}
				len (filter ((function __lambda__ (c) {
					return c.memory.role == 'miner';
				}), current_creeps));
				var sources = room.find (FIND_SOURCES);
				if (Cache.rooms[room_name].current_carry_parts > 0) {
					var spawned = false;
					for (var source of sources) {
						var current_miners = filter ((function __lambda__ (c) {
							return c.memory.role == 'miner' && c.memory.target == source.id && (c.spawning || c.ticksToLive > 50);
						}), current_creeps);
						if (len (current_miners) == 0) {
							var energy_to_use = room.energyCapacityAvailable;
							if (room.memory.no_miner_ticks > 20) {
								var energy_to_use = room.energyAvailable;
							}
							var miner_multiple = min (3, math.floor (energy_to_use / 250));
							var body = [];
							var cost = 0;
							for (var i = 0; i < miner_multiple; i++) {
								body.append (WORK);
								body.append (WORK);
								cost += 200;
							}
							for (var i = 0; i < miner_multiple; i++) {
								body.append (MOVE);
								cost += 50;
							}
							if (room.energyAvailable - used_energy >= cost) {
								var result = spawn.spawnCreep (body, name, {['memory']: {['target_room']: room.name, ['role']: 'miner', ['target']: source.id}});
								if (result == OK) {
									room.memory.no_miner_ticks = 0;
									num_spawns += 1;
									used_energy += cost;
								}
								else if (result == ERR_NOT_ENOUGH_ENERGY && len (current_miners) == 0) {
									if (room.memory.no_miner_ticks == null) {
										room.memory.no_miner_ticks = 0;
									}
									room.memory.no_miner_ticks += 1;
								}
							}
							var spawned = true;
							break;
						}
					}
					if (spawned) {
						continue;
					}
				}
				var miner_multiple = min (3, math.floor (room.energyCapacityAvailable / 250));
				var income = len (sources) * min (10, 4 * miner_multiple);
				if (Cache.rooms[room_name].current_carry_parts < income * 3) {
					var energy_to_use = spawn.room.energyCapacityAvailable;
					if (Cache.rooms[room_name].current_carry_parts == 0) {
						var energy_to_use = spawn.room.energyAvailable;
					}
					var hauler_multiple = min (16, math.floor (energy_to_use / 150));
					var part_change = 0;
					var body = [];
					var cost = 0;
					for (var i = 0; i < hauler_multiple; i++) {
						body.append (CARRY);
						body.append (CARRY);
						body.append (MOVE);
						part_change += 2;
						cost += 150;
					}
					if (room.energyAvailable - used_energy >= cost) {
						var result = spawn.spawnCreep (body, name, {['memory']: {['target_room']: room.name, ['role']: 'hauler'}});
						if (result == OK) {
							num_spawns += 1;
							used_energy += cost;
							Cache.rooms[room_name].current_carry_parts += part_change;
							print ((((spawn.room.name + ' spawned hauler ') + name) + ' with body ') + body_shorthand (body));
						}
					}
					continue;
				}
				if (Cache.rooms[room_name].current_work_parts < income) {
					var worker_multiple = min (16, math.floor (spawn.room.energyCapacityAvailable / 200));
					var body = [];
					var cost = 0;
					var part_change = 0;
					for (var i = 0; i < worker_multiple; i++) {
						body.append (WORK);
						part_change += 1;
						cost += 100;
					}
					for (var i = 0; i < worker_multiple; i++) {
						body.append (CARRY);
						cost += 50;
					}
					for (var i = 0; i < worker_multiple; i++) {
						body.append (MOVE);
						cost += 50;
					}
					if (room.energyAvailable - used_energy >= cost) {
						var result = spawn.spawnCreep (body, name, {['memory']: {['target_room']: room.name, ['role']: 'worker'}});
						if (result == OK) {
							num_spawns += 1;
							used_energy += cost;
							Cache.rooms[room_name].current_work_parts += part_change;
							print ((((spawn.room.name + ' spawned worker ') + name) + ' with body ') + body_shorthand (body));
						}
					}
					continue;
				}
				break;
			}
		}
	}
	if (Game.cpu.generatePixel && Game.cpu.bucket == 10000 && Game.cpu.getUsed () < Game.cpu.limit && ['shard0', 'shard1', 'shard2', 'shard3'].includes (Game.shard.name)) {
		if (Game.cpu.generatePixel () == OK) {
			print (' ======= Generating pixel! Press F to pay respects to your bucket! ======= ');
		}
	}
};
module.exports.loop = main;

exports.Cache = Cache;
exports.body_shorthand = body_shorthand;
exports.main = main;
