"""Check the documented playback selector without a real server or browser."""
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TutorialTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node is optional for JavaScript snippet tests")
    def test_playback_selector_errors_urls_and_preference(self):
        doc = (ROOT / "03-实战示例/01-从登录到播放.md").read_text(encoding="utf-8")
        section = doc.split("## 5. 取播放地址", 1)[1].split("## 6.", 1)[0]
        snippet = re.search(r"```javascript\n(.*?)```", section, re.S).group(1)
        harness = '''
const assert = require('node:assert/strict');
const state = {baseUrl: 'https://emby.example', userId: 'u'};
let response;
async function api() { return response; }
(async () => {
 response = {PlaySessionId: 'p', MediaSources: [{Id:'s', DirectStreamUrl:'/direct', TranscodingUrl:'/transcode'}]};
 let info = await getPlaybackInfo('i');
 assert.equal(info.url, 'https://emby.example/direct');
 assert.equal(info.isTranscoding, false);
 response.MediaSources[0].DirectStreamUrl = 'https://emby.example/absolute';
 assert.equal((await getPlaybackInfo('i')).url, 'https://emby.example/absolute');
 delete response.MediaSources[0].DirectStreamUrl;
 assert.equal((await getPlaybackInfo('i')).isTranscoding, true);
 response.MediaSources[0].TranscodingUrl = 'https://evil.example/steal';
 await assert.rejects(() => getPlaybackInfo('i'), /其他源/);
 response = {MediaSources: []};
 await assert.rejects(() => getPlaybackInfo('i'), /媒体源/);
 response = {ErrorCode: 'NotAllowed'};
 await assert.rejects(() => getPlaybackInfo('i'), /NotAllowed/);
 response = {PlaySessionId: 'p', MediaSources: [{Id:'s'}]};
 await assert.rejects(() => getPlaybackInfo('i'), /播放地址/);
 response = {MediaSources: [{Id:'s', DirectStreamUrl:'/direct'}]};
 await assert.rejects(() => getPlaybackInfo('i'), /PlaySessionId/);
})().catch(e => { console.error(e); process.exitCode = 1; });
'''
        result = subprocess.run([shutil.which("node"), "-e", snippet + harness], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
