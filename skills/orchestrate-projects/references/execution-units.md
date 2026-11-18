# Execution Units

Read when coordination requires multiple execution contexts. Split milestones or tasks for independently observable outcomes, hard dependencies, distinct authority or side effects, or independent resumption. Parallel work units need not each be milestones.

Keep architecture, implementation, integration, and final delivery in the main task by default. Delegate bounded analysis or verification when it pays for the handoff and applicable instructions permit it. Delegate implementation only when interfaces are frozen, no decisions are shared, the work can run independently in parallel, and the main task can verify it cheaply. Create or fork a separate durable host task only when the user explicitly asks and durable visibility or isolation is needed.

Give each unit the execution contract, consequential bounds, required evidence, and where to return results. Reference accessible context that the unit already inherits. For independent review use the [review reference](independent-review.md).

Run checks where the required permissions, login, device, or simulator are available. Carry over relevant context and evidence if an authorized separate task is needed there. Isolate concurrent repository writers by branch and worktree. Verify returned evidence against the current delivered subject and reuse it unless later changes invalidate it or it is incomplete.
