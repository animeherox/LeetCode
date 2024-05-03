class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1parts, v2parts = version1.split("."), version2.split(".")
        len1, len2 = len(v1parts), len(v2parts)
        for i in range(max(len1, len2)):
            v1part = int(v1parts[i]) if i < len1 else 0
            v2part = int(v2parts[i]) if i < len2 else 0
            if v1part < v2part:
                return -1
            elif v1part > v2part:
                return 1
        return 0
