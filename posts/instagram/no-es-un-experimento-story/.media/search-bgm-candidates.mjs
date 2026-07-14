import { heygenAuthHeaders, searchSounds, downloadTo, loadEnvFromDir } from "/Users/achajon/.claude/skills/hyperframes-media/scripts/lib/heygen.mjs";
import { writeFileSync } from "node:fs";

loadEnvFromDir(process.cwd());
const headers = heygenAuthHeaders();

const pools = [
  { id: "a", label: "tension", query: "tense cinematic minor key synth pulse dark moody atmospheric build suspenseful" },
  { id: "b", label: "payoff", query: "confident triumphant modern beat energetic trendy premium product reveal underscore" },
];

const manifest = [];

for (const pool of pools) {
  const results = await searchSounds(pool.query, "music", headers, { limit: 5 });
  console.log(`\nPool ${pool.id} (${pool.label}) — query: "${pool.query}" — ${results.length} results`);
  let i = 0;
  for (const r of results) {
    i++;
    const dest = `.media/candidates/bgm-${pool.id}/${i}-${(r.name || r.description || "track").replace(/[^a-z0-9]+/gi, "-").toLowerCase().slice(0, 40)}.mp3`;
    try {
      await downloadTo(r.audio_url, dest);
      console.log(`  [${i}] score=${r.score?.toFixed?.(3)} dur=${r.duration}s name="${r.name || ""}" desc="${r.description || ""}" -> ${dest}`);
      manifest.push({ pool: pool.id, label: pool.label, query: pool.query, rank: i, score: r.score, duration: r.duration, name: r.name, description: r.description, file: dest, source: "heygen.audio.sounds" });
    } catch (e) {
      console.log(`  [${i}] FAILED download: ${e.message}`);
    }
  }
}

writeFileSync(".media/candidates/bgm-search-manifest.json", JSON.stringify(manifest, null, 2));
console.log(`\nWrote .media/candidates/bgm-search-manifest.json (${manifest.length} candidates)`);
