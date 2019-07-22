import functools
from typing import List, Optional


class Solution:

    def smallestSufficientTeamDFS(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """DFS"""
        skills_indexes = {s: i for i, s in enumerate(req_skills)}
        people_skills_masks = []
        for member in people:
            member_skills_mask = 0
            for s in member:
                if s in skills_indexes:
                    member_skills_mask |= 1 << skills_indexes[s]
            people_skills_masks.append(member_skills_mask)

        @functools.lru_cache(None)
        def dfs(req_skills_mask: int, idx: int) -> Optional[List[int]]:

            # no req skills left
            if req_skills_mask == 0:
                return []

            # got beyond available people
            if idx >= len(people):
                return None

            team_w__member = dfs(req_skills_mask & (~people_skills_masks[idx]), idx + 1)
            team_wo_member = dfs(req_skills_mask, idx + 1)

            if team_w__member is None and team_wo_member is None:
                return None
            if team_w__member is None:
                return team_wo_member
            if team_wo_member is None:
                return team_w__member + [idx]
            if len(team_wo_member) > (len(team_w__member) + 1):
                return team_w__member + [idx]
            return team_wo_member

        return dfs((1 << len(req_skills)) - 1, 0)

    def smallestSufficientTeamDP(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """DP"""
        skills_indexes = {s: i for i, s in enumerate(req_skills)}
        dp = {0: []}

        for i, member in enumerate(people):
            member_skills_mask = 0
            for s in member:
                if s in skills_indexes:
                    member_skills_mask |= 1 << skills_indexes[s]

            for team_skills_mask, team_skills in list(dp.items()):
                team_skills_with_member_mask = team_skills_mask | member_skills_mask
                if team_skills_with_member_mask == team_skills_mask:
                    continue
                if team_skills_with_member_mask not in dp or len(dp[team_skills_with_member_mask]) > (
                        len(team_skills) + 1):
                    dp[team_skills_with_member_mask] = dp[team_skills_mask] + [i]

        return dp[(1 << len(req_skills)) - 1]


def test_one(req_skills: List[str], people: List[List[str]], expected_size: int) -> bool:
    print(req_skills)
    print(people)
    team = Solution().smallestSufficientTeamDFS(req_skills, people)
    if len(team) != expected_size:
        print('team: {}'.format(team))
        print('WRONG! Got team size {}, expected {}.'.format(len(team), expected_size))
        return False
    for skill in req_skills:
        for i in team:
            if skill in people[i]:
                break
        else:
            print('WRONG! Skill {} is missing in team {}.'.format(skill, team))
            return False
    print('OK')
    return True


def test():
    test_one(["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]], 2)
    test_one(["algorithms", "math", "java", "reactjs", "csharp", "aws"],
             [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"],
              ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]], 2)
    test_one(["ldq", "lpah", "i", "ypowcknvrcuouhe", "jftllvrfghmvt", "svscjulmksgo", "xt", "mnfgnpsqhcobst"],
             [["lpah", "xt"], ["ldq", "i"], ["ypowcknvrcuouhe"], ["lpah", "jftllvrfghmvt", "mnfgnpsqhcobst"], ["xt"],
              ["i", "xt"], ["svscjulmksgo"], ["i"], ["i", "ypowcknvrcuouhe"], ["i"], [],
              ["svscjulmksgo", "mnfgnpsqhcobst"], [], ["xt", "mnfgnpsqhcobst"], [],
              ["ypowcknvrcuouhe", "mnfgnpsqhcobst"], ["i"], [], ["jftllvrfghmvt", "svscjulmksgo"],
              ["i", "mnfgnpsqhcobst"], ["jftllvrfghmvt"], ["jftllvrfghmvt"], [], ["i"], ["ypowcknvrcuouhe"],
              ["ypowcknvrcuouhe"], [], [], [], ["ldq", "i"]], 4)


if __name__ == '__main__':
    test()
