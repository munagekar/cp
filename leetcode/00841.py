class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num_rooms = len(rooms)
        visited = [True] + ([False] * (num_rooms - 1))
        num_visited = 1
        q = [0]

        while num_visited < num_rooms and len(q) != 0:
            node_idx = q.pop(0)
            for room in rooms[node_idx]:
                if visited[room]:
                    continue
                num_visited += 1
                visited[room] = True
                q.append(room)

        return True if num_visited == num_rooms else False




