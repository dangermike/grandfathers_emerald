#!/usr/env/bin python3

import sys


class Passage(object):
    def __init__(self, from_room, direction, to_room):
        self.from_room = from_room
        self.direction = direction
        self.to_room = to_room


class Room(object):
    def __init__(self, title, description, usables=None):
        self.title = title
        self.description = description
        self.usables = usables or None


class Game(object):
    def __init__(self, start_room, rooms, passages):
        self._rooms = {}
        self._passages = {}
        for room in rooms:
            self._rooms[room.title] = room
        for passage in passages:
            dirs = self._passages.get(self._rooms[passage.from_room], {})
            dirs[passage.direction] = self._rooms[passage.to_room]
            self._passages[self._rooms[passage.from_room]] = dirs
        self._room = self._rooms[start_room]

    def run(self):
        while True:
            print()
            print('You are in %s' % self._room.title)
            print(self._room.description)
            sys.stdout.write("> ")
            sys.stdout.flush()
            input = sys.stdin.readline().strip("\n").split(' ')
            if len(input) > 0:
                print()
                print('I don\'t know how to ' + input[0])


def main():
    Game(
        'bathroom',
        [
            Room('bathroom', 'the place you put your poop'),
            Room('living room', 'there is a couch with an ogre'),
            Room(
                'lauras room',
                'there is a bed and a window. the bed is on fire'
            ),
        ], [
            Passage('bathroom', 'n', 'living room'),
            Passage('bathroom', 'e', 'lauras room'),
            Passage('living room', 's', 'bathroom'),
            Passage('lauras room', 'w', 'bathroom'),
        ],
    ).run()


if '__main__' == __name__:
    main()
