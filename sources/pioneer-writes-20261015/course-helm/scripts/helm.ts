import { system } from "pocket";

export const helm = system({
    name: "helm", phase: "update", doc: "Puts the helm over every 20th tick.",
    queries: { boats: { with: ["Boat"], fields: ["Boat.rudder"] } },
    run(ctx, { boats }) {
        if (ctx.tick % 20 !== 0) return;
        const b = boats.cols.Boat;
        boats.each((r) => {
            b.rudder[r] = -0.25; // MARK helm-write
        });
    },
});
