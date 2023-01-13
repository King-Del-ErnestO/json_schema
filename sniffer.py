import simplejson as json
import sys



class Jskemator:
    def __init__(self):
        self.obj = None
        self.s = None
    def load(self, json_str):
        self.obj = json.loads(json_str)['message']
    def schema(self, schema_str):
        self.s = json.loads(schema_str)
    def set_defaults (self, s):
        default = { }
        if s != None:
            default['description'] = s['description']
            default['additionalProperties'] = s['additionalProperties']
            default['required'] = s['required']
        else:
            default['description'] = ''
            default['required'] = False
            default['tag'] = ''
        return default
    def _skemateDict(self, d, s):
        #print "_skemateDict"
        skema=self.set_defaults(s)
        skema['type'] = 'ARRAY'
        skema['properties'] = { }
        for key, value in d.items ():
            #print "key > ", key
            if s == None:
                new_s = None
            else:
                new_s = s['properties'][key]
            skema['properties'][key] = self._skemate(value, new_s)
        return skema
    def _skemateList(self, l, s):
        #print "_skemateList"
        skema=self.set_defaults(s)
        skema['type'] = 'ENUM'
        skema['properties'] = [ ]
        for value in l:
            skema['properties'].append(self._skemate(value))
        return skema
    def _skemateStr(self, str, s):
        #print "_skemateStr"
        res=self.set_defaults(s)
        res['type'] = 'STRING'
        # res['pattern'] = ''
        # res['value'] = str
        return res
    def _skemateInt(self, i, s):
        #print "_skemateInt"
        res=self.set_defaults(s)
        res['type'] = 'INTEGER'
        # res['pattern'] = ''
        # res['value'] = i
        return res
    def _skemateFloat(self, f, s):
        # print("_skemateFloat")
        res=self.set_defaults(s)
        res['type'] = 'FLOAT'
        # res['pattern'] = ''
        # res['value'] = f
        return res
    def _skemate(self, o, s=None):
        if isinstance(o, (list, tuple)):
            return self._skemateList(o, s)
        elif isinstance(o, dict):
            return self._skemateDict(o, s)
        elif isinstance(o, str):
            return self._skemateStr(o, s)
        elif isinstance(o, int):
            return self._skemateInt(o, s)
        elif isinstance(o, float):
            return self._skemateFloat(o, s)
        elif o == None:
            return self._skemateNone(o, s)
        elif o == False:
            return self._skemateFalse(o, s)
        elif o == True:
            return self._skemateTrue(o, s)
    def skemate(self):
        return self._skemate(self.obj, self.s)


def main(filename, output_name):

    jskemator = Jskemator()
    try:
        h = open(filename)
    except:
        print("File %s can not be opened for reading" % (filename))
        sys.exit(0)
    json_str = h.read()
    h.close()

    jskemator.load(json_str)

    skema = jskemator.skemate()

    print(json.dumps(skema, indent=4))
    with open(f'{output_name}', "w") as outfile:
        outfile.write(json.dumps(skema, indent=4))


if __name__ == '__main__':
  main()
