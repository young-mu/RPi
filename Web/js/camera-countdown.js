var count = -1;

unitCount();

function unitCount() {
    count++;
    postMessage(count);
    setTimeout(unitCount, 1000);
}
