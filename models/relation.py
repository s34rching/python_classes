class Relation:

    def __init__(self, id, group_id):
        self.id = id
        self.group_id = group_id

    def __repr__(self):
        return '%s:%s' % (self.id, self.group_id)